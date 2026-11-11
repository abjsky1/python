import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 1. 폰트 경로 설정
font_path = r'C:\USERS\ABJSK\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\GMARKETSANSTTFLIGHT.TTF'

# 2. Matplotlib 폰트 매니저에 폰트 강제 추가 (핵심)
fm.fontManager.addfont(font_path)

# 3. 폰트 이름 가져오기 및 글로벌 설정 적용
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 3. Seaborn 테마 설정에 추출한 font_name 적용 및 마이너스 깨짐 방지
sns.set_theme(font=font_name, rc={'axes.unicode_minus': False}, style='whitegrid')

pd.set_option('display.unicode.east_asian_width', True)


#=============================================================================================

# 다중 분류 
fish = pd.read_csv('./day085_261110_python/Fish.csv')
fish.info()

X = fish.drop( columns=['Species'])
Y = fish['Species']
# Y 값의 클래스 종류를 보고 다중인지 판단.

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y, test_size=0.2 , random_state=42 , stratify=Y)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler( )
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)

from sklearn.linear_model import LogisticRegression
# 로지스틱은 이진(시그모이드) 또는 다중(소프트맥스) 에서 자동 선택된다.
# L2규제(릿지) 자동 포함. 손실(오차)함수 계산한다. C = 1.0 기본값 / 하이퍼파라미터
# 계산반복수(경사하강법) : 최적의 가중치/기울기 찾기 위한 계산 반복수 , 기본값 100 / 권장 1000 ~ 3000
# 경사하강법 : 기울기(규제) 변겨앟면서 최적의 기울기/가중치 (오차최소화) 찾는 과정.
model = LogisticRegression( C=1.0 , max_iter=1000 , random_state=42 )
model.fit(X_train_scaled , Y_train)
Y_pred = model.predict( X_test_scaled )

print(Y_pred)

Y_pred_proba = model.predict_proba(X_test_scaled)

print( Y_pred_proba[:3] )
print( Y_test[:3] )

# Y 타겟의 클래스들. 정답지 경우의 수
print( model.classes_ )

# np.round( 리스트 , 자릿수 )
import numpy as np
print( np.round(Y_pred_proba[:3], 3) )





# 평가지표
# average='macro' : 클래스마다 개수 다 다르므로 산술평균 값으로 계산
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score

# 정확도 : 전체 예측 건수 중 맞힌 정답 비율
accuracy_score(Y_test , Y_pred)

# 정밀도 : 예측한 것 중 실제로 맞힌 비율
precision_score(Y_test , Y_pred , average='macro')

# 재현율 : 실제 정답인 것 중에 모델이 놓지지 않고 찾아낸 비율
recall_score(Y_test , Y_pred , average="macro")

# f1 점수 / 표준 : 정밀도와 재현율 간의 조화 조정하기위한 조화평균
f1_score(Y_test , Y_pred , average='macro')

# 4대 평가지표는 혼동 행렬을 사용하여 계산

# 혼동 행렬 시각화
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(Y_test , Y_pred)
plt.grid()
plt.show()

from sklearn.metrics import classification_report
# 리포트 (평가 지도 보고서)
print( classification_report(Y_test, Y_pred) )

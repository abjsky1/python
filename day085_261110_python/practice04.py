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

# PythonML Practice4: 로지스틱 이진 분류 (Logistic Regression)

# 데이터 출처: https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data

#

# [단계 1] 데이터 로드 및 전처리, 독립/종속 변수 추출

# 파일명: ./day085_261110_python/data.csv

import pandas as pd
df = pd.read_csv("./day085_261110_python/data.csv")
df.info()

# 1. 식별자('id') 및 결측 열('Unnamed: 32')이 존재한다면 제외합니다.
df = df.drop(columns=['id'])
df = df.dropna(axis=1, how='all')
df.info()

# 2. 'diagnosis' 열을 종속 변수 y로 추출하고, 악성(M)은 1, 양성(B)은 0으로 매핑(변환)하세요.
df['diagnosis'].head()

# df = df['diagnosis'].str.strip().replace('M', 1)
# df = df['diagnosis'].str.strip().replace('B', 0)
# df['diagnosis'].head(20)
# 어라 안 되네.. ㅋㅋ

df['diagnosis'] = df['diagnosis'].mask(df['diagnosis'] == 'M' , 1)
df['diagnosis'] = df['diagnosis'].mask(df['diagnosis'] == 'B' , 0)
df['diagnosis'].head(20)

df['diagnosis'] = pd.to_numeric(df['diagnosis'])
df.info()
Y = df['diagnosis']

# 3. 'diagnosis'를 제외한 30개의 수치형 피처를 독립 변수 X로 추출하세요.
df_copy = df.drop(columns=['diagnosis']).copy()
df_copy.columns
print(df[ df_copy.columns ])
X = df[ df_copy.columns ]

# 간단한 방법 찾은 것.
X = df.drop(columns=['diagnosis']).copy()

# df = pd.read_csv('./data.csv')

# # id 컬럼 드롭 및 전체가 결측치(NaN)인 열 자동 제거

# df = df.drop(columns=['id'])

# df = df.dropna(axis=1, how='all') # Unnamed: 32 등 모든 값이 NaN인 열을 자동으로 날립니다.

# # 종속 변수(문자열 'M', 'B' 유지) 및 독립 변수 분리

# Y = df['diagnosis']

# X = df.drop(columns=['diagnosis'])


# [단계 2] 훈련용 / 테스트용 데이터 분리

# train_test_split을 사용하여 8:2 비율(test_size=0.2)로 분리하고,
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X, Y , test_size=0.2 , random_state=42 , stratify=Y)

# 재현성을 위해 random_state=42, 클래스 비율 유지를 위해 stratify=y로 설정하세요.

#

# [단계 3] 데이터 표준화 (Standardization)

# StandardScaler를 활용하여 훈련 데이터(X_train) 기준으로 스케일러를 학습(fit)시키고,
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(X_train)
X_train_ss = ss.transform(X_train)
X_test_ss = ss.transform(X_test)

# X_train과 X_test를 각각 표준화(transform) 변환하세요.

#

# [단계 4] 로지스틱 회귀 모델 학습 (Logistic Regression)

# LogisticRegression(random_state=42) 모델을 생성하고 훈련 세트(X_train_scaled, y_train)로 학습시키세요.
from sklearn.linear_model import LogisticRegression
#
model = LogisticRegression()
model.fit(X_train_ss , Y_train)



# [단계 5] 모델 평가 및 분류 정확도(Accuracy) 확인

# 테스트 세트에 대한 예측을 수행하고 정확도(accuracy_score)를 출력하세요.
from sklearn.metrics import accuracy_score
acc = accuracy_score(Y_test , model.predict(X_test_ss))
# 추가로 confusion_matrix 또는 classification_report를 통해 분류 성능을 점검하세요.
from sklearn.metrics import confusion_matrix , classification_report
confusion = confusion_matrix(Y_test , model.predict(X_test_ss))
classification = classification_report(Y_test , model.predict(X_test_ss))
#
print( acc )
print(confusion)
print(classification)


# [단계 6] 학습한 모델의 클래스 및 계수(Weights) 확인

# 모델이 학습한 클래스 종류(classes_)와 절편(intercept_), 주요 피처 계수(coef_) 형태를 출력하세요.
model.classes_
model.intercept_
model.coef_

# >>> model.classes_
# ... 
# array([0, 1])

# >>> model.intercept_
# ... 
# array([-0.24300533])

# >>> model.coef_
# ... 
# array([[ 0.36115007,  0.4822194 ,  0.35315987,  0.43995028,  0.35062156,
#         -0.43954615,  0.78229835,  0.95281283, -0.16399087, -0.08086512,
#          1.23332517, -0.40761126,  0.74829471,  0.90902906,  0.24799098,
#         -0.9069248 , -0.09234069,  0.48208908, -0.33065773, -0.59387632,
#          0.89696783,  1.43409317,  0.72311148,  0.90047661,  0.42020675,
#         -0.17348751,  0.9114058 ,  0.70399881,  1.06126366,  0.05486988]])


# [단계 7] 샘플 데이터 예측 및 예측 확률 확인

# 테스트 세트의 앞선 3개 샘플 데이터에 대해:

# 1. 모델이 예측한 클래스(0 또는 1)를 출력하세요.
model.predict( X_test_ss[:3] )
# array([0, 1, 0])

# 2. 각 샘플별 양성(0)/악성(1) 클래스에 대한 예측 확률(predict_proba)을 출력하세요.
model.predict_proba( X_test_ss[:3] )
# array([[9.99635432e-01, 3.64568116e-04],
#        [1.07465986e-08, 9.99999989e-01],
#        [9.57432053e-01, 4.25679471e-02]])


import numpy as np
print( np.round( model.predict_proba( X_test_ss[:3] ) , 4) )

# 보기 깔끔하게 하기 위해 알아본 것
import numpy as np
np.set_printoptions(suppress=True, precision=4)
print( np.round( model.predict_proba( X_test_ss[:3] ) , 4) )

# 이해하기 쉬운 거
probs = model.predict_proba(X_test_ss[:3])
for p in probs:
    print(f"[{p[0]:.9f}, {p[1]:.9f}]")
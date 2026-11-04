#-------------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm
import requests
from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright
import httpx
import xmltodict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

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

#-------------------------------------------------------------------------------------------


# Practice1
# 1. 데이터 준비
#  - Seaborn 내장 데이터셋인 'tips'를 불러옵니다.
#   import seaborn as sns
#   df = sns.load_dataset('tips')
#  - 독립변수(X, 문제지): 식사 총액 'total_bill' 컬럼 (2차원)
#  - 종속변수(Y, 정답지): 팁 'tip' 컬럼 (1차원)

df = sns.load_dataset('tips')
df.head()
df.info()

X = df[ ['total_bill'] ]
Y = df['tip']
print(X.shape , Y.shape)
print(X.head())
print(Y.head())

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2 , random_state=42)

# 3. 모델 학습 및 수학적 파라미터 확인 
#  - Scikit-learn의 LinearRegression 모델을 생성하고 훈련 데이터로 학습시킵니다.
#  - 학습 완료 후 모델이 도출한 '기울기'와 'y절편'을 출력하세요.
model = LinearRegression( )
model.fit(X_train, Y_train)

print( '가중치 :' , model.coef_ )
print( '편향 :' , model.intercept_ )

# 4. 성능 평가 및 신규 데이터 예측
#  - 테스트 세트(X_test)에 대한 예측값(Y_pred)을 생성하세요.
#  - 실제값(Y_test)과 예측값(Y_pred)을 비교하여 R²(결정계수)와 RMSE(평균 제곱근 오차)를 산출하고 소수점 둘째 자리까지 출력하세요.
#  - 만약 식사 총액이 $30, $100인 새로운 손님이 방문했을 때, 예상되는 팁 금액을 각각 예측하여 출력하세요.
Y_pred = model.predict(X_test)
r2 = r2_score(Y_test, Y_pred)
print( 'r2 :', r2 )
rmse = np.sqrt( mean_squared_error( Y_test , Y_pred ) )
print( 'rmse :', rmse )

print( '식사 총액이 $30, 예상 tip :', model.predict( [ [30] ] ) )
print( '식사 총액이 $100, 예상 tip :', model.predict( [ [100] ] ) )


# 5. 결과 시각화 및 한계점 분석 
#  - Matplotlib을 활용하여 아래 3가지 요소를 하나의 차트에 시각화하세요:
#  1. 테스트 세트의 실제 데이터 산점도 (X_test vs Y_test)
#  2. 식사비 $5부터 $100까지 모델이 예측한 선형 회귀선
#  3. 식사비 $50일 때의 모델 예측 지점 (붉은 점으로 강조)
plt.scatter( X_test , Y_test )
plt.plot( [5,100] , model.predict( [ [5],[100] ] ) , color='orange')
plt.scatter( [50] , model.predict( [ [50] ] ) , color='red')
plt.show( )





# 사이킷런(Scikit-Learn) : 방대한 머신러닝 알고리즘 모델 제공 라이브러리
# 라이브러리 설치 : pip install scikit-learn

# 머신러닝 목표 : 추론/예측 과정

# 특성 : 자료의 모델이 학습하는 자료 정보
# 타깃 : 모델이 궁극적으로 정답을 맞춰야하는 정보

# 중요 3요소
# 1. 모델 사용 이유
# 2. 모델을 사용하기위한 전처리
# 3. 모델의 정확도를 올리기위한 튜닝 방법

# 지도학습 : 특성과 타킷을 모두 제공하여 학습 ( 회귀 / 분류 )
# 비지도학습 : 타깃 없이 특성만으로 제공하는 학습( 군집 / 텍스트분석 / 토픽 / 주성분 QCA? )


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

# 데이터 - Fish.csv
# https://www.kaggle.com/datasets/vipullrathod/fish-market?resource=download

# 데이터 불러오기
df = pd.read_csv( './day081_261104_python/Fish.csv')

print(df.head())

df.info()

# 특성 : Length2 ( 물고기의 대각선 길이 cm )
feature = ['Length2']

# 타깃 : Weight ( 물고기의 무게 g )
target = 'Weight'

print( feature , target )

# x : 독립변수/입력변수/특성
# y : 종속변수/목표변수/타겟
X = df[feature]  # 2차원
Y = df[target]   # 1차원

print( X.shape , Y.shape )

# 데이터 분리
# 학습용/테스트용 분리 : 학습과 평가 자료 구분
from sklearn.model_selection import train_test_split
# 특성학습, 특성테스트, 타겟학습, 타겟테스트 = train_test_split( 특성 , 타겟 , test_size= 비율 , random_state= 난수시드값 )
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2 , random_state = 42 )

# 훈련세트 : 모델에서 규칙 찾는 자료
# 테스트세트 : 모델 학습 이후 모델 평가/예측성능 점수/지표

from sklearn.linear_model import LinearRegression
# 파이썬에서 객체 생성 방법 : 변수명 = 클래스명( )
model = LinearRegression( )
# 모델학습 : .fit( 특성자료 , 타겟자료 )
model.fit( X_train, Y_train )

# 모델 가중치(기울기) 확인 : model.coef_
# 오차/잔차를 최소화하는 기울기 선을 최소제곱법으로 만듦
print( model.coef_ )  # [30.43452394]

# 모델 편향(y절편) 확인 : model.intercept_
print( model.intercept_ )  # -477.30634978973194

# 평가 : 회귀 모델의 score는 결정계수(R²), 1에 가까울수록 좋음
print(model.score(X_train, Y_train))  # 훈련 점수
print(model.score(X_test, Y_test))    # 테스트 점수

# 학습한 모델의 예측
# 새로운 x 값을 넣어서 y 값 구하기
# model.predict( 2차원 특성 자료 )
print( model.predict( [ [30] ] ) )

# 단순회귀모델 : y = ax + b
# y = (30.43452394)x + (-477.30634978973194)

# 시각화
plt.scatter( X_train , Y_train )
# 임의의 예측 점
plt.scatter( [30] , model.predict( [ [30] ] ) , color= 'red' )
# 회귀선 추가 : 임의의 최소값/최대값
plt.plot( [0,100] , model.predict( [ [0] , [100] ] ) , color= 'green' ) 
plt.show()



# 개인 추가 :
# 직선 추가된 시각화 직선 만들기
a = model.coef_[0]      # 기울기 (coef_는 배열이라 [0]으로 값만 꺼냄)
b = model.intercept_    # 절편

# 직선을 그릴 x 범위 : 훈련 데이터의 최솟값 ~ 최댓값
x_line = np.array([X_train['Length2'].min(), X_train['Length2'].max()])
y_line = a * x_line + b     # y = ax + b

plt.scatter(X_train, Y_train, label='train')
plt.scatter([30], model.predict([[30]]), color='red', label='predict (30)')
plt.plot(x_line, y_line, color='orange', label='y = ax + b')
plt.axhline(0, color='gray', linestyle='--')   # y = 0 기준선
plt.xlabel('Length2')
plt.ylabel('Weight')
plt.legend()
plt.show()




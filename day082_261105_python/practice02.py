# PythonML Practice 2: 다항 규제 회귀 기반 성적 예측
# 데이터 출처: https://www.kaggle.com/datasets/shambhurajejagadale/student-performance-prediction-dataset

# 1. 데이터 준비 및 전처리
#  - Kaggle 데이터셋을 불러옵니다.
#    import pandas as pd
#    df = pd.read_csv('./student_dataset_10000_rows.csv')
#  - 범주형 변수를 제외한 6개 수치형 컬럼을 독립변수(X, 문제지)로 추출하세요:
#    ['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']
#  - 시험 성적인 'exam_score' 컬럼을 종속변수(Y, 정답지)로 설정하세요.

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.

# 3. 다항 특성 확장 및 표준화 (고정 차수: degree=2)
#  - PolynomialFeatures(degree=2, include_bias=False)를 사용하여 2차 다항 특성을 생성하세요.
#    * 훈련 세트(X_train)로만 .fit()을 수행하고, X_train과 X_test를 각각 .transform() 하세요.
#  - StandardScaler를 생성하고, 다항 확장된 훈련 세트(X_train_poly) 기준으로 .fit()한 뒤 표준 점수로 변환하세요.
#    * 특성 간 스케일 차이를 맞추기 위해 훈련 세트와 테스트 세트 모두 .transform() 하세요.

# 4. 3가지 모델 학습 및 결정계수(R²) 비교 (고정 규제: alpha=1.0)
#  - 3가지 회귀 모델을 각각 생성하고 스케일링된 훈련 데이터로 학습시키세요:
#    1) LinearRegression()
#    2) Ridge(alpha=1.0, random_state=42)
#    3) Lasso(alpha=1.0, random_state=42)
#  - 각 모델별 훈련 세트 R² 점수(Train R²)와 테스트 세트 R² 점수(Test R²)를 각각 산출하여 비교 출력하세요.

# 5. 임의 대조군 데이터에 대한 3가지 모델 예측 비교
#  - 아래 대조군 샘플 2개를 준비하세요:
#    * 샘플 1 (상위권): study_hours=9, attendance=95, sleep_hours=7, internet_usage=2, assignments_completed=18, previous_score=85
#    * 샘플 2 (하위권): study_hours=2, attendance=60, sleep_hours=5, internet_usage=9, assignments_completed=4, previous_score=50
#  - 각 샘플 데이터를 앞서 학습시킨 동일한 변환기(PolynomialFeatures, StandardScaler)로 변환하세요.
#  - 3가지 모델(LinearRegression, Ridge, Lasso)에 변환된 데이터를 각각 대입하여 예상 시험 성적을 산출하고 비교 출력하세요.



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
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

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

# 1. 데이터 준비 및 전처리
#  - Kaggle 데이터셋을 불러옵니다.
import pandas as pd
df = pd.read_csv('./day082_261105_python/student_dataset_10000_rows.csv')

df.head()
df.info()

#  - 범주형 변수를 제외한 6개 수치형 컬럼을 독립변수(X, 문제지)로 추출하세요:
#    ['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']
X = df[ ['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score'] ]

#  - 시험 성적인 'exam_score' 컬럼을 종속변수(Y, 정답지)로 설정하세요.
Y = df['exam_score']

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 3. 다항 특성 확장 및 표준화 (고정 차수: degree=2)
#  - PolynomialFeatures(degree=2, include_bias=False)를 사용하여 2차 다항 특성을 생성하세요.
#    * 훈련 세트(X_train)로만 .fit()을 수행하고, X_train과 X_test를 각각 .transform() 하세요.
poly = PolynomialFeatures(degree=2, include_bias=False)
poly.fit(X_train)
X_train_poly = poly.transform(X_train)
X_test_poly = poly.transform(X_test)

#  - StandardScaler를 생성하고, 다항 확장된 훈련 세트(X_train_poly) 기준으로 .fit()한 뒤 표준 점수로 변환하세요.
#    * 특성 간 스케일 차이를 맞추기 위해 훈련 세트와 테스트 세트 모두 .transform() 하세요.
ss = StandardScaler( )
ss.fit(X_train_poly)
X_train_scaled = ss.transform(X_train_poly)
X_test_scaled = ss.transform(X_test_poly)

# 4. 3가지 모델 학습 및 결정계수(R²) 비교 (고정 규제: alpha=1.0)
#  - 3가지 회귀 모델을 각각 생성하고 스케일링된 훈련 데이터로 학습시키세요:
#    1) LinearRegression()
model_LinearRegression = LinearRegression()
model_LinearRegression.fit(X_train_scaled, Y_train)
#    2) Ridge(alpha=1.0, random_state=42)
model_Ridge = Ridge(alpha=1.0, random_state=42)
model_Ridge.fit(X_train_scaled, Y_train)
#    3) Lasso(alpha=1.0, random_state=42)
model_Lasso = Ridge(alpha=1.0, random_state=42)
model_Lasso.fit(X_train_scaled, Y_train)
#  - 각 모델별 훈련 세트 R² 점수(Train R²)와 테스트 세트 R² 점수(Test R²)를 각각 산출하여 비교 출력하세요.
Y_pred_LinearRegression_train = model_LinearRegression.predict(X_train_scaled)
r2_LinearRegression_train = r2_score(Y_train, Y_pred_LinearRegression_train)

Y_pred_LinearRegression_test = model_LinearRegression.predict(X_test_scaled)
r2_LinearRegression_test = r2_score(Y_test, Y_pred_LinearRegression_test)

LinearRegression_train_r2 = model_LinearRegression.score(X_train_scaled, Y_train)

LinearRegression_test_r2 = model_LinearRegression.score(X_test_scaled, Y_test)
print("1", r2_LinearRegression_train)
print("2", r2_LinearRegression_test)
print("3", LinearRegression_train_r2)
print("4", LinearRegression_test_r2)

# 5. 임의 대조군 데이터에 대한 3가지 모델 예측 비교
#  - 아래 대조군 샘플 2개를 준비하세요:
#    * 샘플 1 (상위권): study_hours=9, attendance=95, sleep_hours=7, internet_usage=2, assignments_completed=18, previous_score=85
sample_data1 = pd.DataFrame( [ { "study_hours" : 9 , "attendance" : 95 , "sleep_hours" : 7 , "internet_usage" : 2 , "assignments_completed" : 18 , "previous_score" : 85 } ] )
#    * 샘플 2 (하위권): study_hours=2, attendance=60, sleep_hours=5, internet_usage=9, assignments_completed=4, previous_score=50
sample_data2 = pd.DataFrame( [ { "study_hours" : 2 , "attendance" : 60 , "sleep_hours" : 5 , "internet_usage" : 9 , "assignments_completed" : 4 , "previous_score" : 50 } ] )
#  - 각 샘플 데이터를 앞서 학습시킨 동일한 변환기(PolynomialFeatures, StandardScaler)로 변환하세요.
sample1_poly = poly.transform(sample_data1)
sample1_scaled = ss.transform(sample1_poly)
sample2_poly = poly.transform(sample_data2)
sample2_scaled = ss.transform(sample2_poly)
#  - 3가지 모델(LinearRegression, Ridge, Lasso)에 변환된 데이터를 각각 대입하여 예상 시험 성적을 산출하고 비교 출력하세요.
Li1 = model_LinearRegression.predict(sample1_scaled)
Li2 = model_LinearRegression.predict(sample2_scaled)
Ri1 = model_Ridge.predict(sample1_scaled)
Ri2 = model_Ridge.predict(sample2_scaled)
La1 = model_Lasso.predict(sample1_scaled)
La2 = model_Lasso.predict(sample2_scaled)

print( "sample1  =>  Li :", Li1 ,"Ri :", Ri1 ,"La :", La1 )
print( "sample2  =>  Li :", Li2 ,"Ri :", Ri2 ,"La :", La2 )



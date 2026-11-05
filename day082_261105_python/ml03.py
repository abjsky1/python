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

# 항 추가 하는 함수
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures( )
poly.fit( [ [2] ] )
# 기본절편, 원래값, 제곱값
print(poly.transform( [ [7] ] ) )

# 절편 제외
poly = PolynomialFeatures( include_bias= False )
poly.fit( [ [2] ] )
# 원래값, 제곱값
print(poly.transform( [ [7] ] ) )

# 특성 2개인 경우
poly = PolynomialFeatures( include_bias= False )
poly.fit( [ [2,3] ] )
# 원래값1, 원래값2, 제곱값1, 원래값1*원래값2 ,제곱값2
print(poly.transform( [ [3,5] ] ) )

# 특성 3개인 경우
poly = PolynomialFeatures( include_bias= False )
poly.fit( [ [2,3,4] ] )
# 원래값, 제곱값
print(poly.transform( [ [3,5,6] ] ) )

# 수동으로 특성의 제곱항을 만들지 않고 자동(PolynomialFeatures)으로 다항 추가

df = pd.read_csv('./day081_261104_python/Fish.csv')

df.head()
df.info()

# 전처리 과정 생략.

X = df[ ['Length2' , 'Height' , 'Width'] ]
Y = df['Weight']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 과소적합 해결/방지 하고자 항 추가 ==> PolynomialFeatures
poly = PolynomialFeatures( include_bias= False )
# 학습할 특성들의 규칙을 찾음
poly.fit( X_train )
print( poly )
# 배운 규칙으로 데이터 바꿈
print( poly.transform( X_train ) )

X_train_poly = poly.transform( X_train )
X_test_poly = poly.transform( X_test )
print( X_train.shape )       # (127, 3)
print( X_train_poly.shape )  # (127, 9)

# 모델 학습 
# from sklearn.linear_model import LinearRegression
model = LinearRegression( )
model.fit(X_train_poly, Y_train)

# 모델 결정 계수
Y_pred = model.predict(X_test_poly)
r2 = r2_score(Y_test , Y_pred)
print(r2)  # 0.9719372415762594

# 단순 선형 회귀 결정계수 : 0.8199897860284712
    # 직선 공식 (1차 방정식) : Y = wX + b
# 다항 선형 회귀 결정계수 : 0.8249869834428712
    # 곡선 공식 (2차 방정식) : Y = wX^2 + wX + b
# 다항 선형 회귀 결정계수 : 0.9719372415762594
    # 곡선 공식

# 다항의 차수 늘리기 , degree = 10 , (차수N) 제곱까지 항 추가하기
poly = PolynomialFeatures( include_bias= False , degree=10 )
poly.fit(X_train)
X_train_poly2 = poly.transform( X_train )
print( X_train_poly2.shape )   # 특성 9개 => 285항

X_train_poly2 = poly.transform( X_train )
X_test_poly2 = poly.transform( X_test )
print( X_train.shape )       # (127, 3)
print( X_train_poly2.shape )  # (127, 9)

# 모델 학습 
# from sklearn.linear_model import LinearRegression
model = LinearRegression( )
model.fit(X_train_poly2, Y_train)

# 모델 결정 계수
Y_pred = model.predict(X_test_poly2)
r2 = r2_score(Y_test , Y_pred)
print(r2)  # 0.07276663213888512

# 모델 구현에서 다양한 속성값(defree = N) 들을 테스트하여 설계 구현한다.


########
# 1. 테스트 데이터의 실제 무게(x)와 예측 무게(y)
plt.scatter(Y_test, Y_pred, alpha=0.7)

# 2. 완벽하게 맞았을 때의 기준선 (실제값 = 예측값)
min_value = Y_test.min()
max_value = Y_test.max()
plt.plot([min_value, max_value], [min_value, max_value], color="orange", linestyle="--")

plt.xlabel("실제 무게")
plt.ylabel("예측 무게")
plt.title(f"다항 회귀: 실제값 vs 예측값 (R² = {r2:.3f})")
plt.show()
########
# 1. 실제 무게
plt.scatter(X_test["Length2"], Y_test, label="실제 무게")

# 2. 모델이 예측한 무게
plt.scatter(X_test["Length2"], Y_pred, color="orange", marker="x", label="예측 무게")

plt.xlabel("Length2")
plt.ylabel("무게")
plt.legend()
plt.show()
########
# 1. Length2를 최소~최대 사이 100개 값으로 촘촘하게 만들기
length_range = np.linspace(X_train["Length2"].min(), X_train["Length2"].max(), 100)

# 2. 나머지 두 특성은 평균값으로 고정한 표 만들기
X_line = pd.DataFrame({
    "Length2": length_range,
    "Height": X_train["Height"].mean(),
    "Width": X_train["Width"].mean(),
})

# 3. 학습 때와 똑같이 항 추가 (fit 없이 transform만)
X_line_poly = poly.transform(X_line)

# 4. 예측
Y_line = model.predict(X_line_poly)

# 5. 실제 데이터 점 + 회귀 곡선
plt.scatter(X_train["Length2"], Y_train, alpha=0.6, label="학습 데이터")
plt.plot(length_range, Y_line, color="orange", label="다항 회귀선 (Height, Width는 평균 고정)")
plt.xlabel("Length2")
plt.ylabel("무게")
plt.legend()
plt.show()
#########








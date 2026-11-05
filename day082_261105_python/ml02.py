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

import pandas as pd
df = pd.read_csv('./day081_261104_python/Fish.csv')

df.head()

# 특성 , 타겟 분류
X = df[ ['Length2'] ]
Y = df['Weight']

# 훈련용/테스트용 분리
# from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# 단순 회귀 모델
# from sklearn.linear_model import LinearRegression
model = LinearRegression( )

# 학습
model.fit( X_train, Y_train )

# 모델의 결정계수
Y_pred = model.predict( X_test )
# from sklearn.metrics import r2_score
r2 = r2_score(Y_test, Y_pred)
print(r2)


# 특성[X] 에 제곱하여 항 추가
# 배열 연결 방법
# np.column_stack( (배열1 , 배열2) ) 
X_train_ploy = np.column_stack( (X_train**2, X_train) )
print( X_train_ploy )

# 제곱된 모델 학습
model = LinearRegression( )
model.fit( X_train_ploy , Y_train )

# 예측
print( model.predict( [ [30**2 , 30] ] ) )  # [405.27748848]

# 시각화
point = np.arange(int(min(X_test['Length2']))-1,int(max(X_test['Length2']))+1)
point_poly = np.column_stack( (point**2 , point) )
# 특성자료
plt.scatter(X_train, Y_train) 
# 제곱항이 추가된 회귀선
plt.plot(point, model.predict( point_poly ) , color='orange')
plt.show()

# 결정계수
x_test_poly = np.column_stack( (X_test**2 , X_test) )
Y_pred = model.predict( x_test_poly )
r2_poly = r2_score(Y_test, Y_pred)
print(r2_poly)  # 0.8249869834428712


# 단순 선형 회귀 결정계수 : 0.8199897860284712
    # 직선 공식 (1차 방정식) : Y = wX + b
# 다항 선형 회귀 결정계수 : 0.8249869834428712
    # 곡선 공식 (2차 방정식) : Y = wX^2 + wX + b


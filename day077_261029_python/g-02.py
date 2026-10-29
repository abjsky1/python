# seaborn : matplotlib 기반의 시각화 라이브러리
# 설치 방법 : pip install seaborn

import seaborn as sns

print(sns.__version__)


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 윈도우 기준 한글 폰트 설정 및 마이너스 부호 깨짐 방지
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 시본 기본 테마 적용 (폰트 설정 유지)
sns.set_theme(font='Malgun Gothic', rc={'axes.unicode_minus': False}, style='whitegrid')

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 1. 폰트 경로 설정 및 추가
font_path = r'C:\USERS\ABJSK\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\GMARKETSANSTTFLIGHT.TTF'
fm.fontManager.addfont(font_path)

# 2. 추가한 폰트의 정확한 이름 가져오기
font_name = fm.FontProperties(fname=font_path).get_name()

# 3. Seaborn 테마 설정에 추출한 font_name 적용 및 마이너스 깨짐 방지
sns.set_theme(font=font_name, rc={'axes.unicode_minus': False}, style='whitegrid')


np.random.seed(42)
n = 100
df = pd.DataFrame({
  '나이': np.random.randint(20, 60, size=n),
  '소득': np.random.randint(2500, 9000, size=n),
  '신용점수': np.random.randint(500, 850, size=n),
  '멤버십': np.random.choice(['일반', 'VIP'], size=n, p=[0.7, 0.3]),
  '이탈여부': np.random.choice([0, 1], size=n, p=[0.75, 0.25]) # 0: 유지, 1: 이탈
})
# 나이가 많을수록 소득이 높은 경향 부여
df['소득'] += df['나이'] * 40

pd.set_option('display.unicode.east_asian_width', True)

print(df.head())

# 카운트플롯 ( 범주형 빈도 집계 )
# sns.countplot( data= 데이터프레임 , x= "범주형컬럼명" , hue= "빈도컬럼명" , palette= "색상테마")
sns.countplot( data= df , x= "멤버십" , hue= "이탈여부" , palette= "Set3" )
plt.title("멤버십 등급별 이탈빈도")
plt.legend( title= "이탈 여부" , labels= [ '유지(0)' , '이탈(1)'])
plt.show()


# 박스플롯 ( 범주별 수치 분포 )
# sns.boxplot( data= 데이터프레임 , x= '범주형컬럼명' , y= '수치형컬럼명' , hue= '그룹컬럼명' , palette='색상테마' )
sns.boxplot(data=df, x='멤버십', y='소득', hue='이탈여부', palette='Pastel2')
plt.title('멤버십 및 이탈 여부에 따른 소득 분포')
plt.xlabel('멤버십 등급')
plt.ylabel('연소득')
plt.show()


# 히트맵 ( 상관계수 계산 )
# 상관계수 : 하나의 변수가 변하면 다른 변수는 증가/감소 관계 수치화 ( -1(음) , +1(양) )
# +-0.85 이상일 때, 관계가 있다고 판단
# 데이터프레임.corr() : 상관계수 행렬 자동 계산
numeric_df = df[ ['나이' , '소득' , '신용점수'] ]
corr_matrix = numeric_df.corr()
print(corr_matrix)

# sns.heatmap( 상관계수행렬 , cmap = "색상맵" , fmt = "소수점형식" )
sns.heatmap( corr_matrix , annot= True , fmt= '.2f' , cmap= 'coolwarm' )
plt.title('수치형 특성 간 상관계수 히트맵 ! @ # $ % ^ & * ( ) - _ = +')
plt.show()


# 산점도
# sns.scatterplot( data= 데이터프레임 , x= "수치컬럼명" , y= "수치컬럼명" , hue= "그룹컬럼명" , style= "모양그룹열" , s= 점크기 , alpha= 투명도 , palette= "색상테마" )
sns.scatterplot( data= df , x= "나이" , y= "소득" , hue= "이탈여부" , style= "신용점수")
plt.title("나이 vs 소득 산점도")
plt.legend()
plt.show()

# 페어플롯 
# sns.pairplot( data= df , hue= "타겟분할열" , palette= "색상테마" )
sns.pairplot( data= df , hue= "이탈여부" )
plt.show()


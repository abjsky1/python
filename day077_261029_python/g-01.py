# Matplotlib
# 개발자 : 코딩능력
# 분석가 : 차트해석

# 파이썬에서 시각적으로 표현하는 라이브러리
# 확인
import matplotlib
print( matplotlib.__version__ )

import matplotlib.pyplot as plt
# matplotlib 그래프는 한글폰트 지원 안 함.

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 1. 폰트 경로 설정
font_path = r'C:\USERS\ABJSK\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\GMARKETSANSTTFLIGHT.TTF'

# 2. Matplotlib 폰트 매니저에 폰트 강제 추가 (핵심)
fm.fontManager.addfont(font_path)

# 3. 폰트 이름 가져오기 및 글로벌 설정 적용
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False



epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23, 0.20]
val_loss = [0.95, 0.75, 0.60, 0.52, 0.48, 0.45, 0.44, 0.43, 0.44, 0.45]

# plt.figure( figsize=(가로inch, 세로inch) )
plt.figure( figsize=( 7 , 4 ) )
# 선차트 : plt.plot( x축값 , y축값 , label = "계열명" , color = "색상명" , linestyle = "선 종류" , marker = "" )
plt.plot( epochs , train_loss , label = "Train Loss" , color = "blue" , linestyle = "-" , marker = "o" )
plt.plot( epochs , val_loss , label = "손실" , color = "red" , linestyle = "--" , marker = "s" )
# 차트의 제목
plt.title("학습별 모델 손실 추세")
# X 축 제목
plt.xlabel("학습수")
# Y 축 제목
plt.ylabel("손실")
# 격자선
plt.grid( True )
# 범례
plt.legend()
# 차트 실행
plt.show()



classes = ['Cat', 'Dog', 'Bird', 'Fish']
counts = [120, 150, 80, 45]

# 막대차트 : 
plt.bar( classes , counts , width = 0.5 , color = ['#222222' , '#347578' , '#581284' , "#932463"] )
plt.title("클래스별 샘플 수")
plt.xlabel("클래스")
plt.ylabel("샘플 수")
plt.grid( True , alpha = 0.5 )
plt.legend()
plt.show()

# 막대 값 레이블 , plt.bar_label( 막대차트변수 , padding = 막대와 레이블 간격 , fontsize = 폰트크기 )
bars = plt.bar( classes , counts , width = 0.5 , color = ['#222222' , '#347578' , '#581284' , "#932463"] )

plt.bar_label( bars , padding = 3 , fontsize = 8 )
plt.show()


x = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
y = [2.3, 3.8, 5.1, 7.0, 7.8, 9.2, 10.5]

# 산점도차트 : ( 상관관계 )
# plt.scatter( x축값 , y축값 , color = "색상" , s = 점크기 , alpha = 투명도 )
plt.scatter( x , y , color = 'purple' , s = 80 , alpha = 0.8 )
plt.title("산점도차트 그려보기")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()


# 히스토그램 : ( 연속형 수치/값 산도표 )
import numpy as np
heights = np.random.normal(loc=170, scale=5, size=1000)

# plt.hist( 값 , bins = 구간개수 , color = '막대색상' , edgecolor = "테두리색상" , alpha = 투명도 )
plt.hist(heights , bins = 30 , color = 'skyblue' , edgecolor = "black" , alpha = 0.7 )
plt.title("키 데이터의 정규분포 확인")
plt.xlabel("키")
plt.ylabel("빈도수")
plt.grid( axis = "y" , linestyle = ":" , alpha = 0.6 ) 
plt.show()



heights = np.random.normal(loc=170, scale=5, size=1000)
data_with_outliers = np.append(heights, [210, 215, 120])

# 박스플롯 : ( 분포 범위 안에 이상치 )
# plt.boxplot( 값 , )
# vert = True( Vertical, 기본값 )로 설정하면 상자를 세로 방향으로 세워서 출력
# patch_artist=True 옵션을 켜주면 빈 테두리만 있던 상자 내부가 기본 색상으로 채워져 출력
plt.figure( figsize=(6,4) )
plt.boxplot( data_with_outliers , vert = True , patch_artist = True )
plt.title("데이터 이상치 탐지용")
plt.ylabel("값")
plt.grid(axis='y' , linestyle = ':' , alpha = 0.6)
plt.show()


# 한 창에 여러 그래프 표현
# fig , axs = plt.subplot( 행개수 , 열개수 , figsize = ( 가로 , 세로 ) )
fig , axs = plt.subplots( 2 , 2 , figsize = ( 10 , 10 ) )
axs[0,0].plot([1,2,3],[4,5,6])
axs[0,1].bar(['A','B','C'], [30,14,25])
axs[1,0].scatter([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5] , [2.3, 3.8, 5.1, 7.0, 7.8, 9.2, 10.5] , s = 80)
axs[1,1].boxplot( data_with_outliers , vert = True , patch_artist = True )

plt.show()
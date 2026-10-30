import numpy as np
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





# Python 데이터분석 Practice6: 종합예제1
# 문제1 [ 타이타닉 생존 데이터 분석]
# 출처: Kaggle - Titanic: Machine Learning from Disaster

# [2. 가설]
# 가설 1: 여성과 아동의 생존율이 남성보다 월등히 높을 것이다. (사회적 보호 )
# 가설 2: 높은 객실 등급(1등석)을 이용한 승객일수록 생존율이 높을 것이다. (경제적 지위와 안전의 상관관계)
# 가설 3: 특정 항구(사우샘프턴 등)에서 탑승한 승객은 객실 등급 분포에 따라 생존율 차이가 발생할 것이다.

# [3. 자료수집 ]
# 3-1 : https://www.kaggle.com/competitions/titanic/overview
# 3-2 : train.csv 파일 판다스로 불러오기 

# [4. 데이터 전처리]
# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.

# [5. 데이터 시각화 및 분석]
# 5-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
# 5-2 : 연령대별 상세 분석:나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다.데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
# 5-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# 5-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
# 5-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# 3-2 : train.csv 파일 판다스로 불러오기
df = pd.read_csv( './day078_261030_python/train.csv')

print(df.head())

df.info()

df.drop_duplicates().reset_index(drop= True)

df.info()

#    PassengerId  Survived  Pclass                                               Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0            1         0       3                            Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2            3         1       3                             Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3            4         1       1       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4            5         0       3                           Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S


# 수치형 결측치 보정: '나이(Age)' 컬럼의 결측치는 이상치에 강건한(Robust) 분석을 위해 중앙값(Median)으로 대체해야 한다.
# df['Age'].str.strip().replace('', None)  # 문자열이 아니라서 안 되는 건가  # int 타입에는 필요가 없는 문장이라는군.

df['Age'] = df['Age'].fillna( df['Age'].median() )


# 범주형 결측치 보정: '승선 항구(Embarked)' 컬럼의 결측치는 가장 빈번하게 등장하는 최빈값(Mode)으로 대체해야 한다.
df['Embarked'].str.strip().replace('', None)

df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode() )

df.info()

print( df['Embarked'] )

print( np.array( df['Embarked'] ) )

df['Embarked'] = df['Embarked'].fillna( df['Embarked'].mode()[0] )

print( df['Embarked'].mode() )

print( df['Embarked'].mode()[0] )

df.info()


# 5-1 : 생존 분포 분석: 전체 생존자와 사망자의 비중을 파악할 수 있는 막대그래프 를 생성한다.
# error : plt.bar( df['Survived'] , df['Survived'].value_counts() , width=0.5 )
# error : plt.show()

print( df['Survived'] )

sns.barplot(df['Survived'])  # 모양이 이상해
plt.show()

print( np.array(df['Survived']) )
df_servived = df['Survived'].drop_duplicates().reset_index(drop= True)
print(df_servived)
print(np.array(df_servived))

plt.bar( np.array(df_servived) , df['Survived'].value_counts() , width= 0.5 )
plt.show()

df.info()  # 1   Survived     891 non-null    int64  확인.

df['Survived'] =  df['Survived'].astype(str)

df.info()  # 1   Survived     891 non-null    str    변경 완료.


# error : plt.bar( df['Survived'] , df['Survived'].value_counts() , width=0.5 )
# error : plt.show()

print( df['Survived'] )  # 카테고리만 쉽게 뽑아내는 방법이 뭐가 있을까...

plt.bar( np.array(df_servived) , df['Survived'].value_counts() , width= 0.5 )
plt.show()

# 카테고리가 0 , 1 로 나올 수는 없는 건가...........

plt.bar( [ '0' , '1' ] , df['Survived'].value_counts() , width= 0.5 )
plt.show()

# 이렇게 하면 되는데,, 문자열 배열로 어떻게 만들지

# 로드형에게 도움을 받아서 찾아낸 ,,, .index

print( df['Survived'].value_counts() )

print( df['Survived'].value_counts().index )
print( df['Survived'].value_counts().values )

plt.bar( df['Survived'].value_counts().index , df['Survived'].value_counts().values )
plt.title("문제 해결 완료")
plt.xlabel("X축은 문자로 [ '0' , '1' ] 완성")
plt.ylabel("Y축은 컬럼별 총합")
plt.grid(True)
plt.show()

# 색 다르게 하고 범례 표시하기
for name, count in df["Survived"].value_counts().sort_index().items():
    plt.bar(str(name), count, width=0.5, label=str(name))
plt.title(f"{"Survived"} 별 인원 수 (반복문)")
plt.xlabel("Survived")
plt.ylabel("인원 수")
plt.legend(title="Survived")
plt.show()


if len(df["Survived"].value_counts().sort_index()) <= 20:
    colors = plt.cm.tab20(range(len(df["Survived"].value_counts().sort_index())))
else:
    colors = plt.cm.viridis(np.linspace(0, 1, len(df["Survived"].value_counts().sort_index())))
bars = plt.bar(df["Survived"].value_counts().sort_index().index.astype(str), df["Survived"].value_counts().sort_index().values, width=0.5, color=colors)
plt.title(f"{"Survived"} 별 인원 수 (색 목록)")
plt.xlabel("Survived")
plt.ylabel("인원 수")
plt.legend(bars, df["Survived"].value_counts().sort_index().index.astype(str), title="Survived")
plt.show()


sns.countplot( data= df , x= "Survived" , hue= "Survived" )
plt.title(f"{"Survived"} 별 인원 수 (seaborn)")
plt.ylabel("인원 수")
plt.show()


# 5-2 : 연령대별 상세 분석: 나이에 따른 생존/사망 분포를 히스토그램으로 시각화한다. 데이터의 흐름을 파악할 수 있도록 커널 밀도 추정 곡선(KDE)을 포함한다.
df.info()
print(df.head())
plt.hist(df['Age'] , bins= 30 )  # 이러면 y축이 연령별 수잖아.
plt.show()

# 일단 풀이는 
sns.histplot( data= df , x="Age" , hue= "Survived" ,  bins= 10 , kde= True )
plt.show()

# 다른 풀이는
plt.hist( df[ df['Survived'] == '0' ]["Age"] , bins= 20 , label= "사망" , color= 'salmon'  , alpha= 0.4 ) 
plt.hist( df[ df['Survived'] == '1' ]["Age"] , bins= 20 , label= '생존' , color= 'skyblue' , alpha= 0.4 )
plt.show()

# 5-4 (성별): sns.countplot을 사용하여 성별(Sex)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data= df , x= "Sex" , hue= "Survived")
plt.show()

# 5-5 (객실 등급): sns.countplot을 사용하여 객실 등급(Pclass)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data= df , x= "Pclass" , hue= "Survived")
plt.show()

# 5-6 (승선 항구): sns.countplot을 사용하여 승선 항구(Embarked)에 따른 생존 여부(Survived)별 인원수를 시각화한다.
sns.countplot(data= df , x= 'Embarked' , hue= 'Survived')
plt.show()



# # 문제2[ 서울시 공공자전거 대여이력 분석]
# 출처: 서울 열린데이터 광장

# [2. 가설]
# 가설 1: 출퇴근 시간대(08시, 18시 전후)의 자전거 대여량이 다른 시간대에 비해 압도적으로 높을 것이다.
# 가설 2: 특정 지하철역 인근이나 유동인구가 많은 지역의 대여소가 대여량 상위권을 차지할 것이다.
# 가설 3: 이용시간과 이용거리 사이에는 강한 양의 상관관계가 존재할 것이다.

# [3. 자료수집]
# 3-1 : https://data.seoul.go.kr/dataList/OA-15182/F/1/datasetView.do
# https://drive.google.com/file/d/1tXfjwXu5HQUyKupqWeEiNk7ZlN0Xf7xw/view
# 3-2 : 2025년 1월, 2월 대여이력 CSV 파일 로드 (encoding='cp949')

# [4. 데이터 전처리 및 병합]
# 4-1 (병합): pd.concat을 사용하여 분리된 월별 데이터를 하나로 통합하고 인덱스를 재부여한다.
# 4-2 (정제): 결측치의 문자열 표현('\N')을 None으로 치환하고, 성별 데이터를 대문자로 통일 및 결측치를 'U'로 보정한다.
# 4-3 (형변환): 이용시간, 거리 등 주요 수치형 변수는 pd.to_numeric으로 변환하고, 날짜 데이터는 pd.to_datetime으로 객체화한다.
# 4-4 (파생변수): 대여일시에서 시간(Hour) 정보를 추출하여 '대여 시간대' 열을 새롭게 생성한다.

# [5. 데이터 시각화 및 분석]
# 5-1 (성별 분포): sns.countplot을 사용하여 성별에 따른 따릉이 이용 비중을 시각화한다.
# 5-2 (시간대 분석): sns.barplot을 사용하여 24시간 중 어느 시간대에 대여가 집중되는지 분석한다.
# 5-3 (인기 대여소): value_counts().head(10)를 활용하여 가장 활발한 상위 10개 대여소를 가로 막대 그래프로 시각화한다.
# 5-4 (상관관계): sns.heatmap을 통해 이용시간, 이용거리, 시간대 등 수치 데이터 간의 밀접도를 분석한다.

data1 = pd.read_csv('./day078_261030_python/서울특별시 공공자전거 대여이력 정보_2501.csv', encoding='cp949')
data2 = pd.read_csv('./day078_261030_python/서울특별시 공공자전거 대여이력 정보_2502.csv', encoding='cp949')

print(data1.head())
print(data2.head())

data1.info()
data2.info()


# 4-1 (병합): pd.concat을 사용하여 분리된 월별 데이터를 하나로 통합하고 인덱스를 재부여한다.
df = pd.concat( [data1 , data2] , axis=0 , ignore_index= True )
print(df.head())
df.info()
# df = pd.concat( [data1 , data2] , axis=1 , ignore_index= True )
# print(df.head())
# df.info()


# 4-2 (정제): 결측치의 문자열 표현('\N')을 None으로 치환하고, 성별 데이터를 대문자로 통일 및 결측치를 'U'로 보정한다.
print( df["성별"].value_counts(dropna=False) )
df = df.replace("\\N", None)
print( df["성별"].value_counts(dropna=False) )
df["성별"] = df["성별"].str.upper()
print( df["성별"].value_counts(dropna=False) )
# df['성별'] = df['성별'].replace(None , "U")
# print( df["성별"].value_counts(dropna=False) )
df['성별'] = df['성별'].fillna("U")
print( df['성별'].value_counts(dropna=False) )


# 4-3 (형변환): 이용시간, 거리 등 주요 수치형 변수는 pd.to_numeric으로 변환하고, 날짜 데이터는 pd.to_datetime으로 객체화한다.
df.info()
df.head()
df["대여일시"] = pd.to_datetime(df["대여일시"])
df["반납일시"] = pd.to_datetime(df["반납일시"])
df["이용시간(분)"] = pd.to_numeric(df['이용시간(분)'])
df["이용거리(M)"] = pd.to_numeric(df['이용거리(M)'])
df.info()
df.head()

# 4-4 (파생변수): 대여일시에서 시간(Hour) 정보를 추출하여 '대여 시간대' 열을 새롭게 생성한다.
df["대여 시간대"] = df['대여일시'].dt.hour
df.head()
print(df["대여 시간대"].value_counts())
df[ ["대여일시" , "대여 시간대"] ].head(20)
df[ ["대여일시" , "대여 시간대"] ].tail(20)


# 5-1 (성별 분포): sns.countplot을 사용하여 성별에 따른 따릉이 이용 비중을 시각화한다.
sns.countplot(data= df , x= "성별")
plt.show()


# 5-2 (시간대 분석): sns.barplot을 사용하여 24시간 중 어느 시간대에 대여가 집중되는지 분석한다.
sns.barplot(data= df['대여 시간대'].value_counts().sort_index().reset_index() , x= "대여 시간대", y= "count")
plt.show()

print(df['대여 시간대'])
print(df['대여 시간대'].value_counts())
print(df['대여 시간대'].value_counts().sort_index())
print(df['대여 시간대'].value_counts().sort_index().reset_index())



# 5-3 (인기 대여소): value_counts().head(10)를 활용하여 가장 활발한 상위 10개 대여소를 가로 막대 그래프로 시각화한다.
df.info()
df['대여 대여소명'].value_counts() # 자동 내림차순 정렬
df['대여 대여소명'].value_counts().head(10)

sns.barplot(data= df['대여 대여소명'].value_counts().head(10).reset_index() , x= "count" , y= "대여 대여소명" )
plt.show()



# 5-4 (상관관계): sns.heatmap을 통해 이용시간, 이용거리, 시간대 등 수치 데이터 간의 밀접도를 분석한다.
sns.heatmap(data= df[['이용시간(분)', '이용거리(M)', '대여 시간대']].corr() , annot=True , fmt= '.2f')
plt.show()














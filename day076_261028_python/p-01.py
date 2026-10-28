# pandas 설치
# 터미널 입력 : pip install pandas

import pandas as pd
print(pd.__version__)

# pandas : 데이터 조작 및 분석(표형태) 라이브러리

# 데이터프레임 2차원 표
data_list = [ [ 'ant' , 25 , 'seoul'  ] , 
              [ 'bee' , 30 , 'busan'  ] , 
              [ 'cat' , 35 , 'incheon']  ]   # 2차원 리스트 

x = pd.DataFrame( data_list )
print(x)

x = pd.DataFrame( data_list , columns=['name' , 'age' , 'city'] )
print(x)

#-----------------------------------------------------------------------

data_dict = { 
              'name' : [ 'ant'  , 'bee'   ,   'cat'  ] , 
              'age'  : [   25   ,   30    ,     35   ] , 
              'city' : ['seoul' , 'busan' , 'incheon']   } # 딕셔너리 

df = pd.DataFrame( data_dict )
print(x)

# 특정 컬럼의 값들을 추출 , df['열이름']
# Series : 1차원
ages = df['age']
print(ages) 
print(type(ages))           # <class 'pandas.Series'>
print(ages.values)
print(type(ages.values))    # <class 'numpy.ndarray'>


import numpy as np
data_np = np.array( data_list )
df = pd.DataFrame( data_np , columns=['name','age','city'] , index=['A','B','C'] )
print(df)

# 매크로(보통 C언어) -> RPA (사무업무(Excel) 자동화 : 보통 Python)


# 주요 속성
print( df.shape )
print( df.columns )
print( df.index )
print( df.values )
print( df.head( 2 ) )
print( df.tail( 2 ) )

df.info()

# 인덱싱 / 슬라이싱
print( df.iloc[0] )
print( df.iloc[1] )
print( df.iloc[0,2] )
print( df.loc['B'] )
print( df.loc['B','city'] )

print( df.iloc[0:2,0:1] )
print( df.loc['A':'C','name':'age'] )

# 열 추가 , df[새로운열] = 새로운값
df['score'] = [100, 80, 95]
print( df )

# 값 수정 , df[수정할열] = 수정할값
df['age'] = [10, 11, 12]
print( df )

df.loc['B','age'] = 31
print( df )

df.iloc[1,1] = 26
print( df )

# 여러개 수정
df.loc[ ['A','B'] , 'score' ] = [ 50 , 60 ]
print( df )

# 필터링(조건)
print( df['score'] > 90 )
print( df[df['score'] > 90] )
print( df[ (df['score'] > 90) & (df['age'] > 10) ] )
print( df[ (df['score'] < 90) | (df['age'] < 10) ] )

cont = df['age'] >= 40
print( df[ (df['score'] > 90) & cont ] )
print( df[ (df['score'] > 90) | cont ] )

# 필터링 이용하여 새로운 열
df['passed'] = False
df.loc[ df['score'] > 90 , 'passed' ] = True
print(df)

# 컬럼명 변경 , df.rename( )
# df.rename( columns={'기존열이름' : '새로운컬럼명'} )
df = df.rename( columns={'city' : '도시' , 'age' : '나이'} )
print(df)

print( df.describe() )
print( df['나이'].sum() )
print( df['score'].mean() )
print( df['passed'].value_counts() )

# 데이터 병합
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})
print(df1)
print(df2)

# 세로 연결 axis = 0
# 가로 연결 axis = 1
new_df = pd.concat( [df1,df2] , axis= 0 , ignore_index=True)
print(new_df)
new_df = pd.concat( [df1,df2] , axis= 1 )
print(new_df)

# 병합
# pd.merge(df1 , df2 , on='공통컬럼명' , how='방향')
# how : 'inner'(교집합) , 'left' , 'right' , 'outer'()
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df_score = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})
print(df_info)
print(df_score)

import numpy as np
new_df = pd.merge(df_info , df_score , on='ID' , how='inner' )
print(new_df)
new_df = pd.merge(df_info , df_score , on='ID' , how='outer' )
print(new_df)
print( np.isnan(new_df.iloc[3,1]) )

# 정렬
df = pd.DataFrame({ 'name' : [ 'Ant' , 'Bee' , 'Cat' , 'Dog' ],
                     'age' : [   27  ,   27  ,   22  ,   32  ],
                    'score': [   88  ,   95  ,   85  ,   90  ]  })

# df.sort_values( by = '컬럼명' , ascending = True )
new_df = df.sort_values( by = 'age' , ascending = True )
print( new_df )

# 다중 정렬 : age 기준으로 1차 정렬 이후 , 동일한 age 내에서 score 기준으로 2차 정렬
new_df = df.sort_values( by = ['age' , 'score'] , ascending = [True , False] )
print( new_df )

# 컬럼명 정렬 가능
# axis = 0 행 , 1 열
new_df = df.sort_index( axis = 0 , ascending = True )
print(new_df)
new_df = df.sort_index( axis = 1 , ascending = True )
print(new_df)


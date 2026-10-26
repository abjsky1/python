import numpy as np

# 배열의 인덱싱
x = np.array( [10,20,30,40,50] )
print( x[0] )
print( x[1] )
print( x[2] )
print( x[3] )
print( x[4] )
print( x[-1] )
print( x[-2] )
print( x[-3] )
print( x[-4] )
print( x[-5] )
print( x[ [0,2,3] ] )   # 특정 인덱스 선택 가능
print( x[ x > 20 ] )    # 논리 조건 가능

# 2차원 배열 인덱싱
y = np.array( [ [1,2,3] , [4,5,6] , [7,8,9] ] )
print( y[0,0] )
print( y[1,2] )
print( y[-1,-1] )
print( y[ y > 5 ] )
print( len( y[ y > 5 ] ) )

# 1차원 슬라이싱
x = np.array( [10,20,30,40,50] )
print( x[1:3] )
print( x[:4] )
print( x[2:] )
print( x[::2] )

# 2차원 슬라이싱
# array이름[ 행슬라이싱 , 열슬라이싱 ]
y = np.array( [ [1,2,3] , [4,5,6] , [7,8,9] ] )
print( y[ : , 1 ] )  # 행 : 전체 , 열 : 1 
print( y[ 1 , : ] )  # 행 : 1 , 열 : 전체
print( y[ 0:2 , 1:3 ] )  # 행 : 0~1 , 열 : 1~2

# 슬라이싱 주의할점 : 파괴적
a = np.array( [10,20,30,40,50] )
b = a[ 1:4 ]
b[0] = 100
print( a , b )  # [ 10 100  30  40  50] [100  30  40]
a = np.array( [10,20,30,40,50] )
b = a[ 1:4 ].copy()
b[0] = 1000
print( a , b )

# 깊은 복사 얕은 복사 파괴적 비파괴적 알아보기

# 배열의 연산
x = np.array( [2,3,5] )
y = np.array( [1,4,6] )
print( x+y ) 
print( x-y )
print( x*y )
print( x**y )
print( x/y )
print( x%y )
print( np.sqrt(x) ) # 제곱근
print( x > 2 )      # [False  True  True]
print( (x > 1) & (x < 3) )
print( (x == 1) | (x == 3) )
print( x > y )

# 배열 간 비교/연산 : 같은 위치끼리 연산/비교
# 배열과 스칼라(단일 숫자) 비교/연산 : 스칼라 연산/비교 결과


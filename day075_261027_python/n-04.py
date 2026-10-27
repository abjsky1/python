import numpy as np  

# 1차원 배열 통계 함수
x = np.array( [1,2,3,4,5] )
print( np.min( x ) )        # 최소값
print( np.max( x ) )        # 최대값
print( np.argmin( x ) )     # 최소값 위치
print( np.argmax( x ) )     # 최대값 위치
print( np.sum( x ) )        # 합계값
print( np.mean( x ) )       # 평균값
print( np.median( x ) )     # 중앙값
print( np.var( x ) )        # 분산
print( np.std( x ) )        # 표준편차
print( np.sqrt( x ) )       # 양의제곱근(루트)

# 2차원 배열 통계 함수
# np.통계함수( 2차원배열 , axis = 생략시 1차원 평탄화 , 0 : 열마다 , 1 : 행마다 )
y = np.array( [ [1,3,6], [2,4,5] ] )
print( np.min( y ) )
print( np.max( y ) )
print( np.min( y , axis = 0 ) )  # 열마다
print( np.max( y , axis = 1 ) )  # 행마다
print( np.argmin( y ) )
print( np.argmax( y ) )
print( np.sum( y , axis = 0 ) )
print( np.mean( y , axis = 0 ) )
print( np.median( y , axis = 1 ) )
print( np.var( y ) )
print( np.std( y ) )
print( np.sqrt( y ) )


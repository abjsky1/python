import numpy as np

# 병합
x = np.array( [ [1,2] , [3,4] ] )
y = np.array( [ [5,6] , [7,8] ] )
z = np.vstack( [x,y] )
print(z)
z = np.hstack( [x,y] )
print(z)

# 병합
z = np.concatenate( (x,y) , axis = 0 )
print(z)
z = np.concatenate( (x,y) , axis = 1 )
print(z)

# 정렬 , .sort(배열) : 오름차순
x = np.array( [3,1,4,2,5] )
print( np.sort(x) )
print("원본 : ", x)
print( np.sort(x)[ : : -1 ] )
print("원본 : ", x)
print( x.sort() )
print("원본 : ", x)

x = np.array( [3,1,4,2,5] )
z = np.argsort(x)   # 오름차순 기준으로 정렬했을 때, 각 위치 번호
print(z)

x = np.array( [73,95,48,53,84] )
z = np.argsort(x)   # 오름차순 기준으로 정렬했을 때, 각 위치 번호
print(z)

for i in range(0,len(z)) :
    if z[i] == 1 :
        print(x[i])

# 필터링
x = np.array( [10,20,30,40,50] )
print( x > 30 )       # 참 거짓
print( x[ x > 30 ] )  # 참인 것만 가져옴
y = np.array( [ [1,2,3],[4,5,6],[7,8,9] ] )
print( y % 2 == 0 )       # 참 거짓
print( y[ y % 2 == 0 ] )  # 참인 것만 가져옴

# 삼항함수(삼항연산자)
# np.where( 조건 , 참 , 거짓 )
x = np.array( [10,20,30,40,50] )
print( np.where( x > 30 , x , 0 ) ) 
y = np.array( [ [1,2,3],[4,5,6],[7,8,9] ] )
print( np.where( y % 2 == 0 , 0 , 1 ))

# 다수 조건 , & | ~ 
y = np.array( [ [1,2,3],[4,5,6],[7,8,9] ] )
print( y[ ( y % 2 == 0 ) & ( y % 3 == 0 ) ] )
a = y % 2 == 0
b = y % 3 == 0
print( y[ a & b ] )
print( y[ a | b ] )
print( y[ ~a ] )    # 짝수가 아닌 ( 부정문 )
# 주의 : C/JAVA 에서 & 를 비트(0 or 1)연산자로 사용  but  Numpy 에서는 & 를 논리연산자로 사용 (python 기본은 and 사용)
# Numpy 는 파이썬에서 실행되는 구조 ( 중복에 따른 오버라이딩 제한 ) bool vs bool_


t = np.array([True ,False ,False,  True,  True])
tt = np.argsort(t)
print(tt)
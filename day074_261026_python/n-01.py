# 개발자 기준 : python 두고 이해 -> 해당 분야 도메인 활용(프로젝트마다 요구사항 분석에 필요한 도메인 이해)

# 비개발자 기준 : 해당 분야 도메인 이해 -> python 도구 활용

# Numpy 사용 이유 : 수치 계산에 고성능 때문에, 머신러닝이나 딥러닝 예측모델들을 만드는 라이브러리들이 numpy 를 사용하기 때문

# Numpy 설치 
# 터미널에서 pip install numpy
import numpy as np
print(np.__version__)

# numpy 학습하는 이유 : 데이터분석(수치계산) , ML/DL 라이브러리들이 np 를 사용하기 때문에

# 1차원 배열 생성
a1 = np.array( [1,2,3,4] ) 
print(a1)    # [1 2 3 4]

a2 = np.array( [ [1,2,3], [4,5,6] ] )
print(a2)

# 동적타입(자동으로 타입 정해줌) 속도가 느림.
# but numpy 는 정적타입
x = np.array( [1 , True , "안녕"] )
print(x)    # ['1' 'True' '안녕']

# 0 으로 배열로 초기화 가능
x0 = np.zeros( (2,3) )
print(x0)

x1 = np.ones( (3,2) )
print(x1)

b = np.arange(0, 10, 2)
print(b)    # [0 2 4 6 8]

# 시작 끝 구간 나누기
c = np.linspace(0, 1, 5)
print(c)    # [0.   0.25 0.5  0.75 1.  ]

# *튜플or리스트도 가능
d = np.array( (2,3) )
print(d)

# 배열 길이 확인
e = np.array( [ [1,2,3] , [4,5,6] ] ) 
print(e.shape)  # (2, 3)  ==  2행 3열

# 배열 타입 확인
f = np.array( [1.0 , 2.0 , 3.0] )
print(f.dtype)

# 배열 차원 수 확인
g = np.array( [ [ [1] , [2] ] , [ [3] , [4] ] , [ [5] , [6] ] , [ [7] , [8] ] ] )
print(g.size)   # 요소/자료 수
print(g.ndim)   # 차원 수

# 배열의 데이터 타입
# np.array( 리스트/튜플/csv파일 등 , dtype=np.타입명 )
# np.타입명(비트수) , 32bit = 4byte
# np.bool_  : 언더바 주의 ( 파이썬 bool != 넘파이 bool_ )
# np.bytes_ : 영문 또는 일부특수문자(아스키코드) 1바이트  ,  (한글 : UTF8 = 3바이트)
x = np.array( [1,2,3] , dtype=np.int64 )
print(x.dtype)
x = np.array( [ 1.1 , 2.2 , 3.3 ] , dtype=np.float64 )
print(x.dtype)
x = np.array( [True, True, True] , dtype=np.bool_)
print(x.dtype)
x = np.array( ['apple', 'banana', 'orange'] , dtype=np.bytes_ )
print(x.dtype)

# 타입 변환
# .astype(np.새로운타입)
x = np.array( [1.5, 2.3, 3.7] )
y = x.astype(np.int32)
print(y)


# 타입 지정한 이유 :
# - 메모리 효율성 & 속도 & 정밀연산 개선 (빠름)
# - 텐서플로우/파이토치 라이브러리
# - 
# - 



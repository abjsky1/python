import pandas as pd
df = pd.read_csv( "./day085_261110_python/Fish.csv")

df.info()

X = df[ [ 'Length2' , 'Height' , 'Width' ] ]
Y = df[ 'Weight' ]

# 훈련용/검증용 분리
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size= 0.2 , random_state= 42 )

# 과소적합 방지하고자 항 추가 = PolynomialFeatures
from sklearn.preprocessing import PolynomialFeatures
# 기본값 : degree= 2  
poly = PolynomialFeatures( degree= 2 , include_bias= False ) 
poly.fit( X_train )
X_train_poly = poly.transform( X_train )
X_test_poly = poly.transform( X_test )

# 항이 많아지면 항/특성 간에 단위 표준화/스케일링 필요
from sklearn.preprocessing import StandardScaler
ss = StandardScaler( )
ss.fit( X_train_poly )
X_train_scaled = ss.transform( X_train_poly )
X_test_scaled = ss.transform( X_test_poly )

# 모델 선택
# 단순 선형 회귀
# 규제 ( 릿지 , 라쏘 ) alpha 규제 강도
from sklearn.linear_model import LinearRegression
model = LinearRegression( )
model.fit( X_train_scaled , Y_train )

# 결정계수 확인
train_score = model.score( X_train_scaled , Y_train)
test_score = model.score( X_test_scaled , Y_test)

print(train_score , test_score)

# 학습데이터와 테스트데이터의 결정계수 차이를 최소화.


#============= 과정 묶음 =============
from sklearn.pipeline import Pipeline
# pipe_model = Pipeline( [ ( "식별자" , 클래스명() ) ] )
pipe_model = Pipeline( [ 
                         ( "poly" , PolynomialFeatures( degree=2 , include_bias=False ) ) , 
                         ( "sclaer" , StandardScaler( ) ) ,
                         ( "regressor" , LinearRegression( ) ) 
                                                                                            ] )

pipe_model.fit( X_train , Y_train )

train_r2 = pipe_model.score( X_train , Y_train )
test_r2 = pipe_model.score( X_test , Y_test )

print(train_r2 , test_r2)


# 최적(성능좋은/오차적은)의 파아미터(매개변수/대입값) 찾기
# degree=2 , alpha = 0.01

from sklearn.linear_model import Ridge
pipe_model = Pipeline( [ 
                         ( "poly" , PolynomialFeatures( degree=2 , include_bias=False ) ) , 
                         ( "sclaer" , StandardScaler( ) ) ,
                         ( "ridge" , Ridge( ) ) 
                                                                                            ] )

# 후보군 파라미터 만들기
# { '식별자__파라미터명' : [ 후보값 , 후보값 ] }
param_grid = { 'poly__degree' : [ 2 , 3 ] , 'ridge__alpha' : [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ] }

# k-fold 교차검증
from sklearn.model_selection import KFold
# KFold( n_splits= k개의 동일한 폴드로 분할 , shuffle= 분할시 무자구이 섞기 , random_state= 42 )
kf = KFold( n_splits=5 , shuffle=True , random_state=42 )
# 학습 데이터를 5개로 나누어 4개 학습하고 1개로 검증하는 과정을 5번 반복 = 평균 오차/손실 성능

# 그리드서치 CV : 교차검증과 다양한 파라미터를 자동으로 실행하고 최적 찾기.
from sklearn.model_selection import GridSearchCV
# grid = GridSearchCV( estimator= 진행할모델/파이프라인 , param_grid= {후보군 파라미터} , scoring='평가지표명', cv=교차검증 , n_jobs=-1(CPU 사용 가능한 코어의 최대 병렬 사용) )
grid = GridSearchCV( estimator=pipe_model , param_grid=param_grid , scoring='r2', cv=kf , n_jobs=-1 )

# 그리드서치로 학습
grid.fit(X_train , Y_train)

# 주요 속성
best_pipe = grid.best_estimator_
print( grid.best_params_ )
print( grid.best_score_ )

# 최적 모델로 평가
print( best_pipe.score(X_train, Y_train) )
print( best_pipe.score(X_test, Y_test) )


# 서빙 , 학습된 모델 저장하고 다른 곳에서 호출
# 연구/학습 : 코랩(고사양GPU)에서 학습 --> 실제 서버(Fast API)에서 호출
import joblib
# joblib.dump( 저장할모델 , 경로 )
joblib.dump( best_pipe , './day085_261110_python/fish_model.pkl' )



print( list(range(2,10)) )

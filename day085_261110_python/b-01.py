# 로지스틱 회귀 : 범주형을 예측하는 대표적인 분류 알고리즘
import pandas as pd 
df = pd.read_csv('./day085_261110_python/Fish.csv')
df.info()

# 이진 분류 실습하기위한 정답지 2가지 종류만 사용
df = df[ ( df['Species'] == 'Bream' ) | ( df['Species'] == 'Smelt' ) ]

X = df[ ['Weight','Length1','Length2','Length3','Height','Width'] ]
Y = df['Species'] # Bream or Smelt

# 분리 분류 학습모델 사용시 ( 타깃의 분리 비율 일정 만들기 )
# stratify=Y : 타깃 무작위 분리한 경우 클래스(값) 비율 일정 유지 , 분류모델
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 , stratify=Y )

# 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler( )
ss.fit(X_train)
X_train_scaled = ss.transform(X_train)
X_test_scaled = ss.transform(X_test)

# 로지스틱 모델 사용
from sklearn.linear_model import LogisticRegression
model = LogisticRegression( )
model.fit( X_train_scaled , Y_train )
Y_pred = model.predict( X_test_scaled )
print( Y_pred )

# 결과 속성
print( model.classes_ )
print( model.predict_proba( X_test_scaled[ :3] ) )

# [    'Bream'      'Smelt'      ]
# [ [ 0.99255987   0.00744013 ]
#   [ 0.99568698   0.00431302 ]
#   [ 0.04598467   0.95401533 ]  ]

# 정확도 평가 : 결정계수 대신 
from sklearn.metrics import accuracy_score
# accuracy_score( 테스트정답지 , 정답예측 )
acc = accuracy_score( Y_test , Y_pred )
print( acc )

















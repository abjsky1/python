# 앙상블 배깅 또는 부스팅 방식으로 복합 모델 구현
# 부스팅 앙상블 : 순차적으로 학습시키고 오차를 다음 학습에 넘김.
# 설치 : pip install lightgbm xgboost catboost


url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'

import pandas as pd
df = pd.read_csv(url)
df.info()

# alcohol , sugar , pH , class(0:레드 , 1:화이트)

X = df[ [ 'alcohol' , 'sugar' , 'pH' ] ]
Y = df[ 'class' ]

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 , stratify=Y )

# 3가지 부스팅 앙상블 사용
# Classifier : 분류
# Regressor : 회귀
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier, XGBRFRegressor
# n_estimator : 부스팅 사용할 트리 개수 기본값 100 , 실무에서는 1000~3000 권장 ( 최적 모델 탐색 후 중간 종료 )
# learning_rate : 학습률 , 경사하강법에서 오차 보정하기 위한 이동 단위 , LightGBM 기본값 0.1 (모델마다 다름)
# max_depth : 트리의 최대 높이 제한 , LightGBM 기본값 -1 제한없음 ( 과대적합 주의 )
# verbose = -1 : 실행중 트리들이 처리하는 로그 끄기 
models = { "XGBoost"  : XGBClassifier( n_estimator= 100 , learning_rate=0.05 , max_depth=4 , random_state=42 , n_jobs=-1 ) , 
           "LightGBM" : LGBMClassifier( n_estimator= 100 , learning_rate=0.05 , max_depth=4 , random_state=42 , n_jobs=-1 , verbose=-1 ) }



# 반복 이용하여 모델 학습 / 학습 시간 테스트
import time
from sklearn.metrics import f1_score

for name , model in models.items() :
    # 학습 시작 시간
    start = time.time()
    # 학습
    model.fit(X_train , Y_train)
    # 현재 시간에서 시작 시간 제외 (소요시간 구하기)
    end = time.time() - start
    # 예측
    Y_pred = model.predict(X_test)

    print( "=========== 모델명 : " , name )
    print( "> 학습 소요시간 : " , end , "초" )
    print( "> train acc : " , model.score( X_train , Y_train ) )
    print( "> test  acc : " , model.score( X_test  , Y_test  ) )
    print( "> f1_score  : " ,    f1_score( Y_test  , Y_pred  ) )


# =========== 모델명 :  XGBoost
# > 학습 소요시간 :  0.21536540985107422 초
# > train acc :  0.8795458918606889
# > test  acc :  0.8553846153846154
# > f1_score  :  0.905337361530715
# LGBMClassifier(learning_rate=0.05, max_depth=4, n_estimator=100, n_jobs=-1,
#                random_state=42, verbose=-1)
# =========== 모델명 :  LightGBM
# > 학습 소요시간 :  0.07851266860961914 초    빠르다
# > train acc :  0.8795458918606889          
# > test  acc :  0.8607692307692307          과대적합 우수
# > f1_score  :  0.9089079013588324          스코어 우수


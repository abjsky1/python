url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
import pandas as pd
df = pd.read_csv(url)
df.info()

# alcohol , sugar , pH , class(0:레드 , 1:화이트)

X = df[ [ 'alcohol' , 'sugar' , 'pH' ] ]
Y = df[ 'class' ]

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 , stratify=Y )

from lightgbm import LGBMClassifier
# n_estimator : 부스팅 사용할 트리 개수 기본값 100 , 실무에서는 1000~3000 권장 ( 최적 모델 탐색 후 중간 종료 )
# learning_rate : 학습률 , 경사하강법에서 오차 보정하기 위한 이동 단위 , LightGBM 기본값 0.1 (모델마다 다름)
# max_depth : 트리의 최대 높이 제한 , LightGBM 기본값 -1 제한없음 ( 과대적합 주의 )
# verbose = -1 : 실행중 트리들이 처리하는 로그 끄기 
# num_leaves : 기본값 30 , 가질 수 있는 최대 노트 수
# 리프노드가 가질 수 있는 최대 수
# min_child_samples=20 : 리프 노드 최소 샘플 수 
# subsample=0.8 : 매 학습마다 랜덤으로 80% 만 샘플링
# subsample_freq=1 : subsample와 같이 설정하되, 매 트리마다 배깅을 활성화
model = LGBMClassifier(
    # 다양한 매개변수(파라미터) 설정
    n_estimators=1000, #1) 추정기(모델) 최대 개수 설정, 기본값 100, 넉넉 넣고
    learning_rate=0.05, #2) 학습률(각 트리의 축소 비율), 기본값0.1
    num_leaves=15, #3) 하나의 트리(모델) 가질 수 있는 최대 리프 노드수 (과적합 수)
    max_depth=6, #4)하나의 트리 최대 깊이, 기본값-1 (무제한)
    min_child_samples=20, #6) 리프 노드 최소 샘플 수 
    subsample=0.8, #7) 매 학습마다 랜덤으로 80% 만 샘플링
    subsample_freq=1, #8) 7)와 같이 설정하되, 매 트리마다 배깅을 활성화
    colsample_bytree=0.8, #9) 매 학습마다 랜덤으로 전체 특성 중 80% 만 무작위 선택학습
    class_weight="balanced",
    random_state=42, n_jobs=-1, verbose=-1 #) 매 학습마다 로그 숨김
)  

from lightgbm import early_stopping
# eval_set=[ ( X_test , Y_test ) ] : 조기 종료하기위한 (성능) 검증용 데이터셋 포함
#   - 만약에 여러번 학습 중에 손실함수 결과 오차/잔차가 최적이 되면 종료 모니터링
#   - 교차검증과 비슷
# early_stopping( stopping_rounds=50 , verbose=False ) : 학습 과정 중 실행할 콜백 함수
#   - 학습마다 검증 성능이 개선되지 않을 때 추가로 기다릴 반복 횟수
model.fit( X_train , Y_train , eval_set=[ ( X_test , Y_test ) ] , callbacks=[ early_stopping( stopping_rounds=50 , verbose=False ) ] )

# 주요 속성 확인
print( model.best_iteration_ ) # 최적의 트리 반복 수/번호 
print( model.feature_name_ ) # 각 특성의 이름
print( model.feature_importances_ ) # 각 특성의 중요도

# 평가지표
from sklearn.metrics import f1_score
Y_pred = model.predict( X_test )
print( model.score( X_train , Y_train ) )               # 0.8845487781412353
print( model.score( X_test , Y_test ) )                 # 0.8523076923076923
print( f1_score( Y_test , Y_pred , average='macro' ) )  # 0.8192436040044494

# 예측하기
import pandas as pd

new_wine = pd.DataFrame([ [11.5,2.3,3.1] , [13.8,11.2,3.3] ])
new_pred = model.predict( new_wine )
print( '예측1 :', new_pred[0] )  # 0 : red
print( '예측2 :', new_pred[1] )  # 1 : white

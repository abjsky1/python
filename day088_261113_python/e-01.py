# 앙상블 : 배깅 또는 부스팅 방식으로 복합 모델 구현
# 배깅 앙상블 : 여러 트리모델을 병렬 처리하여 최적의 모델 찾기
# 랜덤포레스트 : 


url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
import pandas as pd
df = pd.read_csv(url)
df.info()

# alcohol , sugar , pH , class(0:레드 , 1:화이트)

X = df[ [ 'alcohol' , 'sugar' , 'pH' ] ]
Y = df[ 'class' ]

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 , stratify=Y )

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(
    # 트리의 최대 깊이 제한 ( 과적합 억제 )
    max_depth=3,
    # 클래스 불균형 해소 ( 과접합 억제 )
    class_weight="balanced",
    # 생성할 결정 트리 개수 기본값 100 , 1000~3000
    n_estimators=100,
    # 각 노드에서 분할 시 특성의 최대 개수
    # 분류는 'sqrt' , 회귀는 'log2'
    max_features='sqrt',
    # CPU 최대 사용
    n_jobs=-1,
    # 랜덤 시드
    random_state=42
)
model.fit(X_train , Y_train)
# 분류모델에서는 Accuracy
print( model.score(X_train , Y_train) )  # 0.7852607273426977
print( model.score(X_test , Y_test) )    # 0.7738461538461539

# n_estimators=100
# 0.7852607273426977
# 0.7738461538461539

# n_estimators=10
# 0.817009813353858
# 0.8007692307692308

# max_features='sqrt' 사용하는 이유 : 분류에서 샘플을 사용할 때 샘플들을 전체 사용하지 않는다.
# 총 4개인 경우 랜덤으로 4에서 제곱근 하여 2개만 사용한다.
# 전체 샘플 사용시 과적합이 생길 수 있음.
# 전체 (숲)을 보는 방식이 아닌 무작위(나무) 로 각기 다른 샘플 사용

print(model.feature_names_in_)
print(model.feature_importances_)









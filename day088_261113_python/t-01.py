# 의사결정트리

url = 'https://raw.githubusercontent.com/rickiepark/hg-mldl/master/wine.csv'
import pandas as pd
df = pd.read_csv(url)
df.info()

# alcohol , sugar , pH , class(0:레드 , 1:화이트)

X = df[ [ 'alcohol' , 'sugar' , 'pH' ] ]
Y = df[ 'class' ]

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 , stratify=Y )

from sklearn.tree import DecisionTreeClassifier , DecisionTreeRegressor
# DecisionTreeClassifier : 종속/타겟이 범주형이면 Classifier 사용
# DecisionTreeRegressor  : 종속/타겟이 범주형이면 Regressor 사용

model = DecisionTreeClassifier()
model.fit(X_train , Y_train)
# 분류모델에서는 Accuracy
print( model.score(X_train , Y_train) )  # 0.9978833942659227
print( model.score(X_test , Y_test) )    # 0.8730769230769231

# 훈련용과 테스트 데이터간의 점수 차이가 10% 이상이면 과적합
# 실무에서도 5% 안으로 줄이려고 함.

# 과적합 => 규제
# !!! : 스케일링/표준화 필요없음 => 원본 그대로 비교하여 분류
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
# 트리 모델 시각화 
# plot_tree( model , max_depth=시각화할 최대 깊이 )
plot_tree( model , max_depth=1 , feature_names=[ 'alcohol' , 'sugar' , 'pH' ] )
plt.show()

# 트리 : 전체적인 의사결정 분기 구조
# 노드 : 사각형 상자 하나하나를 의미하며 , 최상단 노드를 Root 노드
# 노드 내부 속성 해석
#   X[0] 또는 특성명 <= 값      ,  분기 조건 ( T:왼쪽 , F:오른쪽 )
#   gini = 값                  ,  지니 불순도 ( 0에 가까울수록 순수, 0.5 혼잡 )
#   samples = 값               ,  해당 노드의 데이터 총 개수
#   values <= [ 개수 , 개수 ]   ,  해당 노드에 도달한 특성 값으로 분류한 특성들의 개수
# 트리의 과정 : gini 불순도를 최대한 0에 가깝게 가지치기 하는 것

# 규제 : 가지치기( 루트 개수 제한 )
model = DecisionTreeClassifier( 
    # 트리의 최대 깊이를 3응로 제한하여 복잡도 낮추기
    max_depth=3 ,
    # 리프노드(마지막노드)가 가져야 할 최소 샘플 수 10개 제한
    min_samples_leaf=10 ,
    # 분할 측정 지표 gini vs entropy
    criterion="gini" ,
    # 난수 시드
    random_state=42
    )

model.fit( X_train , Y_train )
print( model.score(X_train , Y_train) )  # 0.8456802001154512
print( model.score(X_test , Y_test) )    # 0.8407692307692308
# 규제 전 : 12% 차이가 존재
# 규제 후 : 0.5% 차이로 성능개선

# 타겟/종속 클래스의 불균형 ( 레드/화이트 와인 개수/비율 다름 )
# 불균형 완화 작업 추가 
model = DecisionTreeClassifier( 
    # 트리의 최대 깊이를 3응로 제한하여 복잡도 낮추기
    max_depth=3 ,
    # 리프노드(마지막노드)가 가져야 할 최소 샘플 수 10개 제한
    min_samples_leaf=10 ,
    # 분할 측정 지표 gini vs entropy
    criterion="gini" ,
    # 난수 시드
    random_state=42 ,
    # 클래스 빈도에 반비례하여 가중치를 자동 부여
    class_weight="balanced"
    )

model.fit( X_train , Y_train )
print( model.score(X_train , Y_train) )  # 0.787569751779873
print( model.score(X_test , Y_test) )    # 0.7946153846153846
# 점수가 줄었다(?)
# 성능이 0.5% 떨어졌다
# 과소적합 발생.

# 특성 중요도
# 분류 모델에서 예측에 기여한 특성의 중요도를 수치로 알려줌
print(model.feature_names_in_)
# [ 'alcohol' , 'sugar' , 'pH' ]
print(model.feature_importances_)
# [0.06047705 0.92312892 0.01639403]









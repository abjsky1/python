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
print( model.score(X_train , Y_train) )
print( model.score(X_test , Y_test) )

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

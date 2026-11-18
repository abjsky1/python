# 지도학습 : X특성(독립) 과 Y타겟(종속) 모델에 학습하여 예측
# 비지도학습 : X특성(독립) 모델 이용하여 거리/밀도 군집/클러스터/그룹

import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')
df.info()

# 공부시간 , 결석일수 , 1학기성적 , 2학기성적 , 3학기성적
X = df[['studytime', 'absences', 'G1', 'G2', 'G3']] 
# Y/타켓/종속이 없음  ==>  비지도 학습

from sklearn.model_selection import train_test_split
# 학습 98% , 검증 2% ( 중요도 떨어짐 )
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

# 스케일링/단위표준화
#
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)
X_test_scaled = ss.transform(X_test)

# 군집=그룹만들기=클러스터
# k개의 군집을 찾는 KMeans 모델 사용
from sklearn.cluster import KMeans
# 모델 생성
# KMeans( n_clusters = k )
model = KMeans( n_clusters=3 ) 
# 군집
model.fit(X_train_scaled)

train_labels = model.predict(X_train_scaled)
print( train_labels[ : 10] )  # [1 0 0 2 0 0 0 1 1 0]

print("테스트 학생 :" , model.predict(X_test_scaled))  # [1 0 1 1 1 0 0 1]

# 시각화 : 특성 여러개이므로 2D 시각화 한계
# 복습 
import pandas as pd
list_2 = pd.DataFrame([ [2,3] , [4,5] ])
print(list_2.iloc[ : 1])  # 2,3
print(list_2.iloc[ : , 1])  # 
import matplotlib.pyplot as plt
plt.scatter( X_train_scaled[:,4] , X_train_scaled[:,1] , c=train_labels )
plt.scatter( X_test_scaled[:,4] , X_test_scaled[:,1] , c="red" , marker='*' )
plt.show()


# 최적의 K(군집/그룹) 수 찾기 VS 지도학습( F1 분류 / R2 회귀 )
from sklearn.metrics import silhouette_score
sse_list = []
sil_list = []

for k in range(2, 20) :
    # k반복마다 학습 모델 생성
    k_temp = KMeans( n_clusters=k , random_state=42 )
    # 모델 학습/추론 동시에 , fit + predict
    preds = k_temp.fit_predict(X_train_scaled)
    # 군집 결과에 각 샘플과 중심점 거리 제곱의 합 저장
    sse_list.append( k_temp.inertia_ ) 
    sil_list.append( silhouette_score(X_train_scaled , preds) )

# plt.plot( range(2,20) , sse_list , marker='o' )
plt.plot( range(2,20) , sil_list , marker='o' )
plt.show()


import matplotlib.pyplot as plt

# 1행 2열의 서브플롯 생성 (전체 가로 12, 세로 4 크기)
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# 첫 번째 그래프 (왼쪽): Elbow (SSE / Inertia)
axs[0].plot(range(2, 20), sse_list, marker='o')
axs[0].set_title('Elbow Method (SSE)')
axs[0].set_xlabel('k')
axs[0].set_ylabel('SSE (Inertia)')

# 두 번째 그래프 (오른쪽): Silhouette Score
axs[1].plot(range(2, 20), sil_list, marker='o', color='orange')
axs[1].set_title('Silhouette Score')
axs[1].set_xlabel('k')
axs[1].set_ylabel('Silhouette')

plt.tight_layout() # 그래프 간격 자동 조절
plt.show()

# sse : 엘보우지점(기울기가 완만하게 꺾이는 변곡점) 5 ~ 10
# 실루엣 : 높은 값일수록 이상적
# 두 차트 해석하여 최적의 K 해석
# 최적 k 군집하기
best_model = KMeans(n_clusters=9)
pred = best_model.fit_predict(X_train_scaled)
print(pred[:10])
print(X_train_scaled[:10])

# HDBSCAN : 밀도 기반으로 군집 , 이상치(-1) 자동 탐지
from sklearn.cluster import HDBSCAN
# model = HDBSCAN( min_cluster_size= 군집하기위한 최소데이터수 , min_samples= 군집 판별할 때 계산되는 이웃 수 )
model = HDBSCAN(min_cluster_size=15 , min_samples=5 , copy=True)
pred = model.fit_predict(X_train_scaled)
print(pred)  # 군집/그룹 4개 , 이상치 1개(-1)


# 머신러닝 정리
# - 파이프라인 
# - 데이터셋 => 전처리 => 특성/타겟 분리 => 스케일링/원핫인코딩 => 모델학습(파라미터선정) => 모델저장 => 모델불러오기 => 모델로 예측/추론
#
# 지도학습    -  분류  - 종속변수가 범주/카테고리 
#                    - 대표모델 : (대규모) LightBGM , (소규모) Logistic,Tree    
#                    - 평가지표 : F1-score , Accuracy    
#            -  회귀  - 종속변수가 연속적인 수치 
#                    - 대표모델 : (대규모) LightBGM , (소규모) Linear/ridge/lasso
#                    - 평가지표 : R2 , RMSE
# 비지도학습  -  군집  - 종속변수가 없음
#                    - 대표모델 : KMean , HDBSCAN
#                    - 평가지표 : SSE , Silhouette Score
#
# ** 트리모델은 스케일링 필요 없음
# ** 앙상블(LightBGM) 원핫인코딩 자동(카테고리타입)

# 앙상블 : 여러 모델 학습
# - 배깅(Bagging)    :        병렬          - 모델들의 오차값 평균으로 최적 파라미터 선정 
# - 부스팅(Boosting) : Gradient(경사하강법)  - 이전에 모델의 오차를 다음 모델이 보완하며 최적 파라미터 선정

# 튜닝 
# - 앙상블           : optuna
# - Logistic/Linear : (GridSearchCV)


# next step
# 딥러닝

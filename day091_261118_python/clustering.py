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


# 범주형(문자) 특성 갖는 학습 방법

import seaborn as sns
df = sns.load_dataset("penguins")

df.info()
df.head()
# <class 'pandas.DataFrame'>
# RangeIndex: 344 entries, 0 to 343
# Data columns (total 7 columns):
#  #   Column             Non-Null Count  Dtype  
# ---  ------             --------------  -----  
#  0   species            344 non-null    str    
#  1   island             344 non-null    str    
#  2   bill_length_mm     342 non-null    float64
#  3   bill_depth_mm      342 non-null    float64
#  4   flipper_length_mm  342 non-null    float64
#  5   body_mass_g        342 non-null    float64
#  6   sex                333 non-null    str    
# dtypes: float64(4), str(3)
# memory usage: 18.9 KB

# 전처리 : 결측 제외
df = df.dropna().reset_index(drop=True)
df.info()
df.head()
# <class 'pandas.DataFrame'>
# RangeIndex: 333 entries, 0 to 332
# Data columns (total 7 columns):
#  #   Column             Non-Null Count  Dtype  
# ---  ------             --------------  -----  
#  0   species            333 non-null    str    
#  1   island             333 non-null    str    
#  2   bill_length_mm     333 non-null    float64
#  3   bill_depth_mm      333 non-null    float64
#  4   flipper_length_mm  333 non-null    float64
#  5   body_mass_g        333 non-null    float64
#  6   sex                333 non-null    str    
# dtypes: float64(4), str(3)
# memory usage: 18.3 KB

# 다중분류 실습 위한 특성/타겟
X = df.drop( columns=['species'] )
Y = df['species']

from sklearn.model_selection import train_test_split
X_train , X_test , Y_train , Y_test = train_test_split(X , Y, test_size=0.2 , random_state=42 , stratify=Y)

# 복합형 파이브라인 위한 수치형과 범주형 특성 분리
num_features = ['bill_length_mm' , 'bill_depth_mm' , 'flipper_length_mm' , 'body_mass_g']
cat_features = ['island' , 'sex']

# 복합 특성 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
# pp = ColumnTransformer( transformers= [ ( '식별자' , 전처리기 , 컬럼목록 ) ] )
# OneHotEncoder : 범주형 자료들을 0과 1로 표현
# drop = 'first' : 첫번째 범주에 대한 카테고리는 제외
# sparse_output = False : 변환된 자료들을 numpy 배열로 반환 
pp = ColumnTransformer( transformers= [ 
    ( 'num' , StandardScaler( ) , num_features ),  
    ( 'cat' , OneHotEncoder( drop='first' , sparse_output=False ) , cat_features)] )

# 파이프라인 만들기
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
pipe = Pipeline( [ ('pp' , pp) , ('model' , LogisticRegression( C=1.0 , max_iter=1000 , random_state=42 ) ) ] )

pipe.fit(X_train , Y_train)

Y_pred = pipe.predict(X_test)
Y_pred_proba = pipe.predict_proba(X_test)

# 타겟 종류 확인
pipe.classes_

print(Y_pred)
print(Y_pred_proba)

import numpy as np
print(np.round(Y_pred_proba, 3))

# 리포트 (모델 평가 지표)
from sklearn.metrics import f1_score
f1_score(Y_test, Y_pred , average='macro')





import matplotlib.pyplot as plt
import seaborn as sns

# 수치형 변수 4개와 타깃(species) 간의 관계 시각화
sns.pairplot(df, hue="species", palette="Set2", corner=True)
plt.suptitle("펭귄 종별 수치 특성 분포 및 상관관계", y=1.02)
plt.show()
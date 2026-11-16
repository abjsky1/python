import pandas as pd
url = 'https://raw.githubusercontent.com/rashida048/Datasets/master/USA_cars_datasets.csv'
df = pd.read_csv(url)

df = df[df['price'] > 0]

# 수치형데이터
num_cols = ['year', 'mileage']
# 범주형데이터
cat_cols = ['brand', 'model', 'title_status', 'color', 'state']
# *만약에 모델의 성능 향상하기 위한 도메인 지식의 (계산식) 특성 추가 좋다.

# 범주형 자료들을 원핫인코딩이 아닌 판다스'카테고리' 타입 변경
# 트리구조에서는 수치형 데이터 스케일링 할 필요 없음.
# 원핫인코딩도 내장되어있어 할 필요 없음.
for col in cat_cols: 
    df[col] = df[col].astype('category')

print( num_cols + cat_cols )
X = df[num_cols + cat_cols]
Y = df['price']
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# optuna 튜닝
# 1. optuna 설치 : pip install optuna shap
import optuna
optuna.logging.set_verbosity( optuna.logging.WARNING )

# 목적함수 만들기 : 각 탐색 시도마다 교차 검증 수행 후 평균 성능 반환 , *콜백함수( trial )
def objective( trial ) :
    pass

# optuna.create_study(direction='maximize/minimize')
optuna.create_study(direction='maximize')
# 현재 실습은 회귀모델이며 r2결정계수 평가지표 사용할 예정
sampler = optuna.samplers.TPESampler( seed=42 )
Study = optuna.create_study( direction='maximize', sampler=sampler )
# Study.optimize( 목적함수 , n_trials= 반복수(최소100단위) )
Study.optimize( objective , n_trials= 20 ) # 반복수 만큼 목적함수 실행


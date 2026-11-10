import joblib
# 모델 불러오기
# joblib.load( '모델경로.pkl' )
model = joblib.load( './day085_261110_python/fish_model.pkl' )

import pandas as pd
# 불러온 모델로 예측 테스트
sample = pd.DataFrame( { 'Length2': [32.5] , 'Height': [10.0] , 'Width': [4.2] } )

predict = model.predict(sample)

print( predict )
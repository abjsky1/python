# '텍스트 마이닝' 실습에 필요한 데이터셋
import pandas as pd
url = "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt"
# 리뷰 데이터셋
# rating : 평점
df = pd.read_table(url, names=['rating', 'review'])
# 평점 3 제외
df = df[df['rating'] != 3]
# 평점 4 이상은 긍정 , 평점 2 이하 부정
df['label'] = (df['rating'] >= 4).astype(int)
# 전체데이터셋에서 특정 n개 샘플링
df_sample = df.sample(n=5000, random_state=42).reset_index(drop=True)


df_sample.info()
df_sample.head()

# <class 'pandas.DataFrame'>
# RangeIndex: 5000 entries, 0 to 4999
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   rating  5000 non-null   int64
#  1   review  5000 non-null   str  
#  2   label   5000 non-null   int64
# dtypes: int64(2), str(1)
# memory usage: 117.3 KB

# 텍스트에서 전처리 = 정규표현식
# 정규표현식 : 특정한 규칙을 가진 문자열의 집합을 표현하는 형식 언어

# 정규표현식 함수 호출
import re
# 정귤표현식 통과한 목록
cleaned_list = [ ]
for text in df_sample['review'] :
    # re.sub(r'[ 표현식 ]','치환문자' , str() )
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]',' ', str(text))
    # .join() : 각 리스트 항목 사이에 특정 문자로 연결
    # .split() : 하나의 문자열 안에 특정 문자로 분리하여 리스트 반환
    cleaned_text = ' '.join( text.split() )
    cleaned_list.append( cleaned_text )

df_sample['cleaned_review'] = cleaned_list
print( df_sample.head(3) )

# 한국어 형태소 분석기
# KoNLPy  :  자바기반  
# Kiwi    : C언어기반
# Kiwi (Korean Intelligent Word Identifier)
# 설치 : pip install kiwipiepy
from kiwipiepy import Kiwi
# 고성능 한국어 형태소 분석기 객체 생성
kiwi = Kiwi()
# 사전 학습에 없는 단어 추가
for word in ['가성비' , '내돈내산' , '총알배송'] :
    # kiwi.add_user_word( 새로운단어 , '품사키워드')
    kiwi.add_user_word( word , 'NNG')

# 불용어 제외
from kiwipiepy.utils import Stopwords
kiwi_stopwords = Stopwords()
nabba = {'우웩' , '그냥' , '에바' , '헐'}

# kiwi 이용한 형태소 분석 함수
def tokenize_kiwi( text ) :
    # kiwi.tokenize( 분석할문장 , stopwords= 불용어객체 )
    tokens = kiwi.tokenize( text , stopwords= kiwi_stopwords )
    # print(tokens) # 나중에 확인해볼 것 
    # 추출할 품사 키워드
    # 일반명사 NNG, 고유명사 NNP, 동사 VV, 형용사 VA, 일반부사 MAG
    target_tags = { 'NNG' , 'NNP' , 'VV' , 'VA' , 'MAG' }

    result = []
    for t in tokens : 
        # t.tag : 품사 , t.form 형태소 문자열 반환
        if t.tag in target_tags and t.form not in nabba :
            if len( t.form) > 1 or t.form in { '못' , '잘' , '안' , '왜' , '것' } :
                # 파이썬 삼항 연산자 : 참일 때 표현식 if 조건 else 거짓일 때 표현식
                word = t.form + '다' if t.tag in {'VV' , 'VA'} else t.form
                result.append(word)

    return result

print( df_sample['cleaned_review'].iloc[0] )

print( tokenize_kiwi( df_sample['cleaned_review'].iloc[0] ) )

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(df_sample['cleaned_review'], df_sample['label'], test_size= 0.2, random_state=42 , stratify=df_sample['label'])

# 리뷰 --> 행렬(벡터) 변환
from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf = TfidfVectorizer( tokenizer= 토큰나이즈함수 )
tfidf = TfidfVectorizer( 
                         # 생략시 공백/띄어쓰기 기준으로 분리
                         # 중복 단어 자동 제거.
                         tokenizer= tokenize_kiwi , 
                         # 실행중 발생하는 로그 비활성화
                         token_pattern= None
                         )
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

print( X_train_tfidf.shape )  # (4000, 4110)
print( X_test_tfidf.shape )   # (1000, 4110)

print( '추출한 단어 10개 :', tfidf.get_feature_names_out()[:10] )
# ['가게' '가겨' '가격' '가격대' '가관' '가구' '가까이' '가끔' '가늘다' '가능']
# 문제점 : 오타 등 유사한 단어들을 분별 불가능. 다른 단어로 취급함.
# 해결 : 유사도 거리 계산 ( 임베딩/BERT )


# 긍정/부정 : 감정분석
# 편의를 위해 Logistic 사용
# 실무에서는 lightGBM 사용
from sklearn.linear_model import LogisticRegression  
model = LogisticRegression( C=1.0 , max_iter=1000 , random_state=42 )
model.fit( X_train_tfidf , Y_train )

print( model.score(X_train_tfidf , Y_train) )   # 0.89225
print( model.score(X_test_tfidf , Y_test) )     # 0.834

Y_pred = model.predict(X_test_tfidf)

from sklearn.metrics import f1_score
print('f1 :', f1_score(Y_test , Y_pred))    # f1 : 0.8263598326359832

print( X_train_tfidf.toarray()[0][:10] )

# 예측하기 
new_review = [
    "배송도 정말 빠르고 가성비 최고입니다! 재구매 의사 있어요.",
    "마감 상태가 엉망이고 실밥이 다 터져서 왔네요. 최악입니다.",
    "그냥 가격만큼 하는 것 같아요. 특별히 좋지도 나쁘지도 않음."
]

# 정규표현식 
cleaned_new = [ ]
for text in new_review : 
    text = re.sub( r'[^가-힣a-zA-Z0-9\s]', ' ', str(text) )
    cleaned_new.append( ' '.join( text.split() ) )

# 정규표현식 이후 토큰나이즈
new_tfidf = tfidf.transform( cleaned_new )

# 토큰나이즈 이후 모델 추론
# predict : 추론
# predict_proba : 추론 확률
probs = model.predict_proba( new_tfidf )

# 0.6 이상이면 긍정 , 0.4 이하이면 부정 , 그외 중립
# 리뷰 수만큼 반복
for i in range( len(new_review) ) :
    # i번째 추론 결과 확률 
    # 0인덱스 부정확률 , 1인덱스 긍정확률
    pos = probs[i][1]
    if pos >= 0.6 :
        contents = '긍정'
    elif pos <= 0.4 :
        contents = '부정'
    else :
        contents = '중립'

    print( f'리뷰 : {new_review[i]}' )
    print( f'감정분석 : { contents } , 긍정확률 : { pos } , 부정확률 { probs[i][0] }' )

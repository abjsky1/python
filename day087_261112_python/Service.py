# 비지니스 로직 == 머신러닝 모델 예측
# 클래스 생성
import pandas as pd

class ItemService : 
    # 생성자
    def __init__(self):
      # 멤버변수 선언
      # self.변수명 = 값
        self.df = pd.DataFrame( [ 
            { "id" : 1 , "name" : "콜라" , "price" : 1000 } ,
            { "id" : 2 , "name" : "환타" , "price" : 2000 }
        ] )

    # 함수
    def items( self ) :
        # .to_dict(orient='records') : 
        # - pandas 에 있는 것을 행마다 dictionary(JSON) 형태로 반환
        return self.df.to_dict(orient='records')

    def save( self , item ) :
        # 저장할 딕셔너리를 df 로 변경
        saveDf = pd.DataFrame( [item] )
        self.df = pd.concat( [self.df , saveDf] , ignore_index=True )
        return True

    def update( self , item ) :
        # 수정할 id 조회
        uid = item.get('id')
        # 수정할 id 가 없으면
        if uid not in self.df['id'].values :
            return "수정할 상품이 없습니다."
        # 현재 df 에 입력받은 수정할 id 가 같은 index 조회
        idx = self.df[ self.df['id'] == uid ].index
        # 찾은 인덱스의 값을 수정
        # item.keys() : 딕셔너리.keys() => [속성명, 속성명]
        # item.values() : 딕셔너리.values() => [속성값, 속성값]
        self.df.loc[ idx , item.keys() ] = item.values()
        return True

    def delete( self , id ) :
        if id not in self.df['id'].values :
            return False
        # 존재하면 해당 id 행 제외
        self.df = self.df[ self.df['id'] != id ]
        return True

#----------------------------------------------------------------
# 클래스 밖
# 서비스 객체 생성
# 인스턴스 직접 만들기
item_service = ItemService()

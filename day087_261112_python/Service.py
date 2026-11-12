# 비지니스 로직 == 머신러닝 모델 예측
# 클래스 생성
import pandas as pd

class ItemService : 
    # 생성자
    def __init__(self):
      # 멤버변수 선언
      # self.변수명 = 값
        self.df = pd.DataFrame( [ 
            { 'id' : 1 , 'name' : '콜라' , 'price' : 1000 } ,
            { 'id' : 2 , 'name' : '환타' , 'price' : 2000 }
        ] )

    # 함수
    def items( self ) :
        # .to_dict(orient='records') : 
        # - pandas 에 있는 것을 행마다 dictionary(JSON) 형태로 반환
        return self.df.to_dict(orient='records')

#----------------------------------------------------------------
# 클래스 밖
# 서비스 객체 생성
# 인스턴스 직접 만들기
item_service = ItemService()

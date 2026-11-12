import uvicorn
from fastapi import FastAPI

# fastAPI 객체 생성
app = FastAPI()

# 서버 실행 함수
if __name__ == '__main__':
    uvicorn.run( "f-02:app" , host="127.0.0.1" , port=8000 , reload=True )

# 서버 실행 , 현재 파일(.py) 실행 

# HTTP REST 구현
# REST : 자원을 주고 받는 상태 구조
# REST API : HTTP 로 REST 구현한 것

# FastAPI객체 안에 get/post/put/delete 메소드 지원
# @app.get("/매핑주소")
@app.get("/")
# async def 함수명() : 비동기 함수 선언
async def index() :
    # 반환값
    return "안녕 파이썬 웹"

# 코드 작성 이후 서버 재실행 없이 "reload=True" 속성을 적용했으므로 서버에 자동 반영

# 쿼리스트링
@app.get("/user")
# 파이썬은 동적 타입이지만 "변수명:타입명" 지정타입 가능
async def user( name , age:int ) : 
    info = { 'name' : name , 'age' : age , 'msg' : "*쿼리 통신 성공*" }
    # 딕셔너리가 JSON 타입으로 자동 반환
    return info
# http://localhost:8000/user

@app.get("/item/{name}/{age}")
async def item( name : str , age : int | None = None ) :
    return { 'name' : name , 'age' : age , 'msg' : '*경로 통신 성공*' }

# 본문 , HTTP GET/DELETE => 쿼리/경로
# HTTP POST/PUT => 쿼리/경로/본문BODY
@app.post("/products")
# 전달받은 body본문(json) 값을 파이썬 dict 타입으로 매핑
async def products( product:dict) :
    product['msg'] = "*본문 통신 성공*"
    return product
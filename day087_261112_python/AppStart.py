# 파이썬 파일 분리
# AppStart.py    : FastAPI 실행 파일
# Controller.py  : HTTP REST 파일
# Service.py     : 로직 파일

from fastapi import FastAPI
import uvicorn

app = FastAPI( )
if __name__ == "__main__":
    uvicorn.run( 'AppStart:app' , host="127.0.0.1" , port=8000 , reload=True )

# 컨트롤러에 라우터 연결
# import 파일명
import Controller
# app.include_router( 파일명.변수명 )
app.include_router( Controller.router )


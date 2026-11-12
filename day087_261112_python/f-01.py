# JAVA 비동기 서버 엔진 : Apache Tomcat

# Fast API : HTTP 의 비동기 통신을 지원하는 프레임워크
# 설치 : pip install fastapi uvicorn

from fastapi import FastAPI
import uvicorn

# JAVA : new 클래스() 
# PYTHON : 클래스()
# FastAPI 객체 만들기
app = FastAPI()

# uvicorn 서버 실행 함수 만들기
# 파이썬 main함수 만들기
# 자바의 main 함수 역할 : 자바의 메인 스레드를 포함하여 소프트웨어 프로세스 실행시 최초 실행 함수
# 파이썬 if __name__ == "__main__" : 
# - 해당 파일(.py)이 실행되면 먼저 진입되는 구역
if __name__ == "__main__" : 
  # uvicorn.run( "현재파일명:fastAPI변수명" , host="127.0.0.1" , port=8000 , reload=자동재실행 )
    uvicorn.run( "f-01:app" , host="127.0.0.1" , port=8000 , reload=True )

# 서버 실행 방법 : uvicorn.run 존재하는 파일에서 py 진행
# http://localhost:8000
# 서버 종료 방법 : 해당 서버 터미널에서 'Ctrl + C' 또는 터미널 닫기
# 서버 REST API : http://localhost:8000/docs
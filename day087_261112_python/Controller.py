# 라우터 : 특정 도메인(주소)을 묶어주는 역할
from fastapi import APIRouter
# router = APIRouter( prefix= '/공통URL')
router = APIRouter( prefix= '/api')

# 다양한 REST API CRUD 제공
# 서비스 객체 불러오기
# from 파일명 import 변수명/함수명
from Service import item_service

# 전체조회
@router.get('/items')
async def items():
    # 서비스 안에 함수 호출
    return item_service.items()


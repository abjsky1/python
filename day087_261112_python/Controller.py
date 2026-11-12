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

# 저장
@router.post("/save")
async def save( item:dict ) :
    return item_service.save( item )

# 수정
@router.put("/update")
async def update( item:dict ) :
    return item_service.update( item ) 

# 삭제
@router.delete("/delete")
async def delete( id:int ) :
    return item_service.delete( id )


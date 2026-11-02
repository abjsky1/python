# 웹 크롤링 : 웹페이지에 존재하는 데이터들을 수집하는 기술
# HTML/CSS 기초 지식
# 파이썬 크롤링 라이브러리 : 
# 정적( request / BeautifulSoup )
# 동적( Seleium , Playwright )

# 방법
# 1. 크롤링할 페이지의 도메인주소/robots.txt 검색 후 크롤링 가능 여부 확인 
# ex)  https://www.jobkorea.co.kr/robots.txt
#      User-agent:사용자/브라우저/AI
#      Disallow: 불가능 , Allow: 가능
# 2. 개발자도구(F12)  ==>>  CTRL + SHIFT + C  ==>>  크롤링 요소 선택  ==>>  선택자/식별자 확인
# 3. 저작권 문제 조심

# 라이브러리 설치
# 1. pip install requests
# 2. pip install beautifulsoup4
# 2-1. https://www.crummy.com/software/BeautifulSoup/bs4/doc/ 



# naver 검색 정보 크롤링
# 1. 크롤링 하려는 페이지(주소)가 정적인지 동적인지 확인
# 1-1. 불필요한 파라미터 정리해서 주소 가져오기.
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8&ackey=d0h8w8xs
# https://search.naver.com/search.naver?query=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8

url = "https://search.naver.com/search.naver?query=%EC%95%88%EC%96%91+%EB%82%A0%EC%94%A8"
# 2. requests 라이브러리로 해당 주소 요청하기

import requests
response = requests.get( url )
print( response )  # <Response [200]> : 통신 정상
# 요청한 주소의 HTML 문자로 반환
print( response.text )

# 3. 요청 성공했으면 요청한 페이지의 HTML 파싱하기
# 요청된 URL의 HTML 파싱 라이브러리
from bs4 import BeautifulSoup
# BeautifulSoup( 요청한 결과의 내용물 , 'html.parser' )
# 요청한 URL 결과 문자열들을 HTML 형식으로 변환
soup = BeautifulSoup( response.text , 'html.parser' )
print( soup )

# 4. 파싱한 이유 : 특정한 식별자(마크업) 의 
# soup.select( 선택자 ) : 여러개 추출 
# soup.select_one( 선택자 ) : 한개 추출
text = soup.select_one(".temperature_text")
print( text )

# 5. 마크업 사이의 텍스트 추출
# 추출한 DOM.get_text() 
print( text.get_text() )





# yes24 베스트셀러 도서 정보 크롤링 / 페이징처리(반복문)
# 1. 크롤링 하려는 페이지(주소)가 정적인지 동적인지 확인
# 1-1. 불필요한 파라미터 정리해서 주소 가져오기.
# 1-2. 파라미터 주소 분석하기 
# https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=1&pageSize=24&type=day
# categoryNumber=001 (국내도서)
# categoryNumber=002 (외국도서)
# pageNumber=1 (반복문에 사용)
# https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber=1
import requests
# 요청된 URL의 HTML 파싱 라이브러리
from bs4 import BeautifulSoup

book_list = [ ]

for page in range(1, 4) :
    url = f"https://www.yes24.com/product/category/daybestseller?categoryNumber=001&pageNumber={page}"

    # 2. URL 요청
    response = requests.get( url )

    # 3. HTML 파싱
    soup = BeautifulSoup( response.text , 'html.parser' )

    # 4. 파싱한 이유 : 특정한 식별자(마크업) 의 
    # soup.select( 선택자 ) : 여러개 추출 
    # soup.select_one( 선택자 ) : 한개 추출
    books = soup.select(".item_info")
    print( books )

    # 5. 여러개 추출한 마크업에서 특정한 마크업 추출
    for book in books :
        title = book.select_one('.gd_name').get_text()
        price = book.select_one('.yes_b').get_text()
        auth = book.select_one('.info_auth').get_text().strip().replace("\n","").replace("\r","")

    book_list.append( { "제목" : title , "가격" : price , "저자" : auth } )

print(book_list)

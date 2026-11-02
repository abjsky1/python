# 동적 페이지 크롤링 , 대기/이벤트 존재하는 상태.

# 라이브러리 설치
# 셀레니움과 비슷한 동적 페이지 조작 라이브러리
# pip install playwright
# 크롬(구글회사브라우저)과 비슷한 백그라운드 브라우저(크로미움)
# playwright install
# 비동기 라이브러리
import asyncio
# 비동기 동적 페이지 라이브러리
from playwright.async_api import async_playwright

# naver 검색 정보 크롤링
# 1. 크롤링 하려는 페이지(주소)가 정적인지 동적인지 확인
# 1-1. 불필요한 파라미터 정리해서 주소 가져오기.
# https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=%EC%A7%B1%EA%B5%AC
# https://search.naver.com/search.naver?ssc=tab.image.all&query=%EC%A7%B1%EA%B5%AC

url = "https://search.naver.com/search.naver?ssc=tab.image.all&query=%EC%A7%B1%EA%B5%AC"

# 2. 비동기 함수 만들기
# async def 함수명() : 함수 선언하고 동기화
async def run( ) :
    # 
    item_list = [ ]
    # async_playwright() 실행하고 종료되기 전까지 동기화 처리
    async with async_playwright() as p :
        # 크로미움( 구글 회사 제공하는 백그라운드용 오픈소스 브라우저 )
        # await p.chromium.lanuch( headless = True (백그라운드모드) / False (뷰모드) )
        browser = await p.chromium.launch( headless = False )
        # 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기
        page = await browser.new_page()
        # 빈 페이지에 특정한 URL 주소 대입/이동
        await page.goto( url ) 
        # 스크롤 내리기 , 2번
        for i in range( 2 ) :
            # await page.wait_for_timeout( 밀리초 ) : 밀리초만큼 대기상태 걸어주는 함수 
            await page.wait_for_timeout( 2000 ) 
            # await page.evaluate( "JS코드삽입" )
            # window.scrollTo( 가로 , 세로 ) : 스크롤 이동 함수
            # document.body.scrollHeight : 현재 페이지의 스크롤 세로 높이
            # window.scrollTo( 0 , document.body.scrollHeight ) : 현재 스크롤을 페이지
            await page.evaluate( "window.scrollTo( 0 , document.body.scrollHeight )" )
            

            items = await page.query_selector_all(".tile_item")
            print( items )

            for item in items :
                title = await item.query_selector( '.info_title' )
                # .inner_text() : 특정한 마크업의 사이 텍스트 추출
                title = await item.inner_text()
                img = await item.query_selector( 'img._fe_image_tab_content_thumbnail_image' )
                # .get_attribute() : 특정한 마크업의 속성값 추출
                img = await item.get_attribute( '.src' )
                item_list.append( { '제목' : title , "이미지링크" : img } )

    return item_list 

# *** asyncio.run( 동기화함수() ) ***
item_list = asyncio.run( run() )
print( item_list )


# 중고나라 검색 정보 크롤링
# 1. 크롤링 하려는 페이지(주소)가 정적인지 동적인지 확인
# 1-1. 불필요한 파라미터 정리해서 주소 가져오기.
# https://web.joongna.com/search/%EC%BD%94%EC%B9%B4%EC%BD%9C%EB%9D%BC?minPrice=1000&maxPrice=2000&page=1


# 2. 비동기 함수 만들기
# async def run( ) :
# asyncio.run( run() )

# async def 함수명() : 함수 선언하고 동기화
async def run( ) :
    # 사용자로부터 콘솔에 입력받기
    keyword = input( "중고 제품명 : " )
    min_price = input( "최소 가격 : " )
    max_price = input( "최대 가격 : " )
    

    # async_playwright() 실행하고 종료되기 전까지 동기화 처리
    async with async_playwright() as p :
        # 크로미움( 구글 회사 제공하는 백그라운드용 오픈소스 브라우저 )
        # await p.chromium.lanuch( headless = True (백그라운드모드) / False (뷰모드) )
        browser = await p.chromium.launch( headless = False )
        # 기존 브라우저 선언 아래에 추가
        browser = await browser.new_context(
                                            viewport={"width": 1920, "height": 1080},
                                            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
                                            )
        # 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기
        page = await browser.new_page()
        # 빈 페이지에 특정한 URL 주소 대입/이동
        await page.goto( f'https://web.joongna.com/search/{keyword}' ) 
        # 3초 대기상태
        await page.wait_for_timeout( 3000 ) 

        # 입력받은 값으로 웹페이지에 채우기
        # HTML 에 placeholder 이용하여 특정 마크업 식별
        # page.get_by_속성명("속성값")
        # DOM.fill(값)
        # page.get_by_placeholder("최소 가격").fill( ) : placeholder 에 '최소 가격' 이면 입력받은 값으로 채움
        await page.get_by_placeholder('최소 가격').fill(min_price) 
        # 1초간 일시정지
        await page.wait_for_timeout( 1000 ) 
        # page.get_by_placeholder("최대 가격").fill( ) : placeholder 에 '최대 가격' 이면 입력받은 값으로 채움
        await page.get_by_placeholder('최대 가격').fill(max_price) 
        # 1초간 일시정지
        await page.wait_for_timeout( 1000 ) 
        # 특정한 마크업 클릭 이벤트 실행
        # 텍스트 '적용' 갖고 있는 마크업 선택
        # Dom.click() : 
        await page.get_by_text("적용").click()
        await page.wait_for_timeout( 3000 ) 
        # 제품 사진, 제품명, 제품 가격 추출
        # href^='/시작주소/'  : 시작주소로 시작하는 모든 주소 식별
        items = await page.query_selector_all("div.group > div > a[href^='/product/']")
        # print(items)
        for item in items :
            title = await item.query_selector( '.typo-body-sm-medium-14' )
            title = await title.inner_text() if title else "제품명 없음"
            price = await item.query_selector( '.typo-title-lg-semibold-18' )
            price = await price.inner_text() if title else "가격 없음"
            img = await item.query_selector( 'img' )
            img = await img.get_attribute( 'src' ) if img else "이미지 없음"
            print(title, price, img)

        # 직접 브라우저 종료
        await browser.close()


asyncio.run( run() )

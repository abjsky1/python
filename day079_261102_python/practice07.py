# Practice7 문제 [ 씨네21(Cine21) 영화 평점 및 핵심 정보 수집 ]
# 출처 및 대상: 씨네21 영화 평점 페이지,  https://cine21.com/movie/point

# 비동기 라이브러리
import asyncio
# 비동기 동적 페이지 라이브러리
from playwright.async_api import async_playwright

# [1. 목표]
# Playwright의 비동기 제어와 동적 페이지네이션(click)을 활용해 여러 페이지를 순회한다.
# 영화 아이템 카드에서 제목, 이미지 링크, 전문가 평점 3가지 핵심 데이터를 정확히 추출하여 구조화한다.

url = "https://cine21.com/movie/point"

async def run( ) :
    # 리스트 생성
    item_list = [ ]
    # async_playwright() 실행하고 종료되기 전까지 동기화 처리
    async with async_playwright() as p :
        # 크로미움( 구글 회사 제공하는 백그라운드용 오픈소스 브라우저 )
        # await p.chromium.lanuch( headless = True (백그라운드모드) / False (뷰모드) )
        browser = await p.chromium.launch( headless = True )
        # 기존 브라우저 선언 아래에 추가
        browser = await browser.new_context(
                                            viewport={"width": 1920, "height": 1080},
                                            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
                                            )
        # 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 열기
        page = await browser.new_page()
        # 빈 페이지에 특정한 URL 주소 대입/이동
        await page.goto( url ) 
        # 3초 대기상태
        await page.wait_for_timeout( 3000 ) 

# [2. 데이터 수집 요구사항]
# 2-1 (페이지 순회): 1페이지부터 3페이지까지 반복문을 통해 동적으로 페이지를 이동한다.

        for i in range(1 , 4) :

            # 교수님 풀이 방법
            # buttonList = await page.query_selector_all( '.pagination .page a' )
            # for i in range(1,4) :
            #     await buttonList[i-1].click()
            #     await page.wait_for_timeout( 3000 )

            if i > 1 :
                await page.locator(f'.pagination .page a[href="javascript:fetch_point_list({i})"]').click()
                await page.wait_for_timeout( 3000 )


# 2-2 (요소 추출): 각 영화 카드 내부에서 아래 3가지 요소를 각각 수집한다.
# 영화 제목 # 이미지 # 전문가 평점

            # href^='/시작주소/'  : 시작주소로 시작하는 모든 주소 식별
            items = await page.query_selector_all("div.list_with_upthumb_item")
            # print(items)

            for item in items :
                title = await item.query_selector( '.title' )
                title = await title.inner_text() if title else "제목 없음"
                star  = await item.query_selector( '.star_wrap:has-text("전문가") > .num' )
                star  = await star.inner_text() if star else "전문가 평점 없음"
                img   = await item.query_selector( '.img_thumb' )
                img   = await img.get_attribute( 'src' ) if img else "이미지 없음"


# 2-3 (데이터 적재): 수집된 데이터를 딕셔너리로 묶어 리스트에 저장하고 최종 출력한다.

                item_list.append( { '제목' : title , "이미지링크" : img , "전문가평점" : star } )
    
        # 직접 브라우저 종료
        await browser.close()

    return item_list 
    
# *** asyncio.run( 동기화함수() ) ***
item_list = asyncio.run( run() )
print( item_list )

        


        












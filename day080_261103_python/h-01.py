# httpx : 외부 API 통신하는 라이브러리
#     ex) API연동 / SPRING API
# httpx 설치
# pip install httpx
import httpx
# httpx 라이브러리에는 .json() 타입변환 가능하지만 .xml() 타입변환은 지원 안 함.
# xmltodict 설치
# pip install xmltodict
import xmltodict
# pandas 라이브러리
import pandas as pd


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# 1. 폰트 경로 설정
font_path = r'C:\USERS\ABJSK\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\GMARKETSANSTTFLIGHT.TTF'

# 2. Matplotlib 폰트 매니저에 폰트 강제 추가 (핵심)
fm.fontManager.addfont(font_path)

# 3. 폰트 이름 가져오기 및 글로벌 설정 적용
font_name = fm.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# 3. Seaborn 테마 설정에 추출한 font_name 적용 및 마이너스 깨짐 방지
sns.set_theme(font=font_name, rc={'axes.unicode_minus': False}, style='whitegrid')

pd.set_option('display.unicode.east_asian_width', True)





service_key = "d6c2201b5bd4dc55ebe5bad723290794837a16fbff6e75fd429dde0e5bfb16b3"
# 공공데이터에 json 형식의 자료 요청
def test1() : 
    # https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?page=1&perPage=10&serviceKey=d6c2201b5bd4dc55ebe5bad723290794837a16fbff6e75fd429dde0e5bfb16b3
    # https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?
    # page=1
    # &perPage=10
    # &serviceKey=d6c2201b5bd4dc55ebe5bad723290794837a16fbff6e75fd429dde0e5bfb16b3
    url = "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?"
    url += "page=1"
    url += "&perPage=10"
    url += f"&serviceKey={service_key}"

    # httpx 이용하여 통신하기
    # httpx.HTTP메소드명(통신할주소) , 통신 결과 반환
    response = httpx.get(url)
    # print( response )

    # 응답 결과 JSON 파싱
    response_json = response.json()
    # print( response_json )

    # 판다스에 저장하기
    df = pd.DataFrame( response_json['data'] )
    print(df.head())
    df.info()
    

test1()





#

def test2() :
    # https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?serviceKey=d6c2201b5bd4dc55ebe5bad723290794837a16fbff6e75fd429dde0e5bfb16b3&pageNo=1&numOfRows=10
    # https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?
    # serviceKey=d6c2201b5bd4dc55ebe5bad723290794837a16fbff6e75fd429dde0e5bfb16b3
    # &pageNo=1
    # &numOfRows=10

    url = "https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown?"
    url += f"serviceKey={service_key}"
    url += "&pageNo=1"
    url += "&numOfRows=10"

    response = httpx.get(url)

    # 요청 응답 자료를 문자열로 반환하여 파이썬 dict 형식으로 변환
    response_dict = xmltodict.parse( response.text )
    print(response_dict)

# <response>
    # <header>
        # <resultCode></resultCode>
        # <resultMsg></resultMsg>
    # </header>
    # <body>
        # <items>
            # <item>    

    df = pd.DataFrame( response_dict['response']['body']['items']['item'] )
    df.info()


test2()









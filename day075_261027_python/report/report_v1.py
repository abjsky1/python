# [ 종합실습: 데이터 분석 최종 보고서 작성 요구사항 ]
# 1. 보고서 필수 포함 항목
# 보고서에는 반드시 다음의 4가지 섹션이 포함되어야 합니다.
# 
# Section 1: 프로젝트 개요
# 분석 주제: 팀이 선정한 주제(자율 주제) 명시
# 데이터 출처: 참고한 데이터 소스(공공데이터포털, Kaggle 등) 및 데이터의 신뢰성 언급
# 
# Section 2: 주요 분석 결과 (Step 1 ~ Step 5 요약)
# 각 단계별로 도출된 핵심 수치를 명확히 제시하세요.
# 
# Section 3: 결과 해석 및 인사이트 예시
# 현상 분석: Step 1(평균/최대)과 Step 4(복합 위험군 %) 결과를 볼 때, 현재 상황이 얼마나 심각한지 설명하세요.
# 타겟팅: Step 5에서 정규화 점수 0.9 이상으로 선별된 그룹이 왜 '최우선 관리 대상'이 되어야 하는지 논리적으로 설명하세요.
# 
# Section 4: 정책 및 솔루션 제안
# 분석 결과를 바탕으로 구체적인 해결책을 제안하세요.
# 예시: "이탈 위험군이 20%로 나타났으므로, 이들을 위한 맞춤형 할인 쿠폰 발송 시스템 구축 제안"
# 
# 보고서 양식 : 링크고서 양식 : 링크, 
# https://docs.google.com/document/d/1bcDQDdHcB4ze0OCX883sSUlDvSKu-JG1Nb23YMv5lkM/edit?usp=sharing


import numpy as np
# [기본 제공 코드] CSV 파일 로드 (헤더 제외, 콤마 구분)
data = np.genfromtxt('./day075_261027_python/report/report.csv', delimiter=',', skip_header=1)
# 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
print(f"데이터 형태: {data.shape}")

print( ~np.isnan(data) )

data16 = ~np.isnan(data)[:,4]
print(data16)

data_without_nan16 = data[data16]
print(data_without_nan16)
print(data_without_nan16[:,4])

data_16 = data_without_nan16[6:,4]
print(len(data_16))

avg_16 = np.mean(data_16)
print(avg_16)
max_16 = np.max(data_16)
print(max_16)



dan = data_without_nan16[ ( data_without_nan16[:,4] < 65 ) | ( data_without_nan16[:,4] > 95 ) ]
print(dan)
print( len(dan) )



data16 = ~np.isnan(data)[:,4]
data17 = ~np.isnan(data)[:,5]
data1617 = ( data16 == True ) & ( data17 == True )
print(data1617)

data_without_nan1617 = data[data1617]
print(data_without_nan1617)

dangerous = data_without_nan1617[:,5] - data_without_nan1617[:,4]
print(dangerous)
print( np.min(dangerous))
print( np.argmin(dangerous) )
print( data_without_nan1617[np.argmin(dangerous)] )
print( data_without_nan1617[np.argmin(dangerous)][0] )

# abs_dangerous = np.abs(dangerous)
# print(abs_dangerous)
# print( np.argmax(abs_dangerous) )
# print( data_without_nan1617[np.argmax(abs_dangerous)] )
# print( data_without_nan1617[np.argmax(abs_dangerous)][0] )

high_risk = ( data_without_nan1617[:,4] < np.mean(data_without_nan1617[:,4]) - 15 ) & ( data_without_nan1617[:,5] < np.mean(data_without_nan1617[:,5]) - 15 )
print( high_risk )
print( data_without_nan1617[high_risk] )
print( len(data_without_nan1617[high_risk])/len(data_without_nan1617)*100 , "%" )



# 공식 : ( x - 최솟값 ) / ( 최댓값 - 최솟값 )

정규화 = ( dangerous - np.min( dangerous ) ) / ( np.max( dangerous ) - np.min(dangerous) )
print(정규화)
print(정규화 < 0.1)
print(data_without_nan1617[정규화 < 0.1])
print(len(data_without_nan1617[정규화 < 0.1]))
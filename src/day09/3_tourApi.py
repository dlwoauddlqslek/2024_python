# 공공데이텊포털 : https://www.data.go.kr
# 출입국관광통계서비스 검색
# 활용신청
import json
import urllib.request

인증키='nwPZ%2F9Z3sVtcxGNXxOZfOXwnivybRXYmyoIDyvU%2BVDssxywHNMU2tA55Xa8zvHWK0bninVkiuZAA4550BDqIbQ%3D%3D'

# [code2]
def getRequestUrl(url):
    요청객체=urllib.request.Request(url)
    try:
        응답객체=urllib.request.urlopen(요청객체)

        if 응답객체.getcode()==200:
            return 응답객체.read().decode('utf-8')
    except Exception as e:
        return None

# [code3] 지정한 날짜, 지정한 국가, 구분 을 받아서 url 요청
def getTourismStateItem(yyyymm,nat_cd,ed_cd):
    # 1. 출입국관광통계의 기본 url
    base='http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'
    # 2. 매개변수: 인증키, 연월,국가코드,출입국구분코드
    parameters=f'?_type=json&serviceKey={인증키}'
    parameters+=f'&YM={yyyymm}&NAT_CD={nat_cd}&ED_CD{ed_cd}'
    url=base+parameters # 3. 합치기
    print(f'url: {url}')

    responseDecode=getRequestUrl(url) # 4. url 요청 후 응답객체 받기
    if responseDecode==None: return None # 5. 만약 응답객체가 None이면 None 반환
    else: return json.loads(responseDecode) # 6. 만약 응답객체가 존재하면 json형식을 파이썬 객체로 변환하는 함수
        # JSON=문자열타입
        # PY: json.loads() JSON형식 --> PY형식 반환 함수, json.dumps() PY형식 --> JSON형식 반환 함수
        # JS: JSON.parse() JSON형식 --> JS형식 반환 함수, JSON.stringify() JS형식 --> JSON형식 반환 함수

# [code4]
def getTourismStateService(nat_cd, ed_cd, nStartYear, nEndYear):
    jsonResult=[] # 수집한 데이터를 저장할 리스트 객체
    dataEND=f'{str(nEndYear)}{str(12)}' # 마지막 연도의 마지막 월(12)
    isDataEnd=0 # 데이터의 끝 확인하는 변수
    for year in range(nStartYear,nEndYear+1): # 시작연도 부터 마지막연도 까지 반복
        print(f'year: {year}')
        for month in range(1,13): # 1~13(미만), 1~12월까지 반복
            print(f'month: {month}')
            if(isDataEnd==1): break # 만약 isDataEnd가 1이면 반복문 종료
            # 0>2 오른쪽정렬 >, 2 자릿수, 0 빈칸이면 0으로 채움 # 1 -> 01, 10 ->10
            yyyymm=f'{str(year)}{str(month):0>2}'
            print(yyyymm)

            jsonData=getTourismStateItem(yyyymm,nat_cd,ed_cd)
            if jsonData!=None:
                print(f'jsonData: {jsonData}')
                # 만약에 지정한 날짜의 내용을
                if jsonData['response']['body']['items']=='':
                    isDataEnd=1 # 지정한 날짜에 내용물이 없으므로 반복문 종료
                    print('데이터 없음')
                    break
                # 내용물이 있으면
                natName=jsonData['response']['body']['items']['item']['natKorNm'].replace(' ','') # 국가명 # 공백 제거
                num=jsonData['response']['body']['items']['item']['num'] # 관광객수
                # 딕셔너리: 국가명, 국가코드 ,연도월, 방문자수
                dic={'nat_name':natName,'nat_cd':nat_cd,'yyyymm':yyyymm,'visit_cnt':num}
                print(dic)
                jsonResult.append(dic) # 딕셔너리를 리스트에 담기
                print(jsonResult)
    return jsonResult


# [code1]
def main():
    # 서비스 요청시 필요한 매개변수들을 입력받기
    nat_cd= int(input("국가코드(중국: 112/일본: 130/미국: 275): ")) # 2. 국가코드(공식 문서 참고)
    nStartYear=int(input('시작연도: ')) # 3. 데이터 수집 시작 연도
    nEndYear=int(input('종료연도: ')) # 4. 마지막 데이터의 연도
    ed_cd='E' # 5. 구분( E: 방한외래관광객(입국), D: 해외 출국 )

    # 6. 서비스 요청후 응답 객체 받기
    jsonResult = []  # 1. 수집한 데이터를 저장할 리스트 객체
    jsonResult=getTourismStateService(nat_cd,ed_cd,nStartYear,nEndYear)
    print(f'jsonResult: {jsonResult}') # 확인

    # 7. 응답받은 py객체를 json으로 변환 후 파일처리
    with open(f'{nat_cd}-{nStartYear}-{nEndYear}.json',"w",encoding="utf-8") as file:
        jsonFile=json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        file.write(jsonFile)

if __name__=="__main__":
    main()




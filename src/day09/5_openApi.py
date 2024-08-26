# 연습문제: 서울 열린데이터 광장에서 '민주주의 서울 자유제안'을 크롤링하여 JSON파일로 저장


import json
import urllib.request

인증키='48616e74716c6a6d33376e66664478'

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
def getTourismStateItem(start,end):
    # 1. 출입국관광통계의 기본 url
    base='http://openAPI.seoul.go.kr:8088/48616e74716c6a6d33376e66664478/json/ChunmanFreeSuggestions'
    # 2. 매개변수: 인증키, 연월,국가코드,출입국구분코드
    parameters=f'/{start}/{end}'
    url=base+parameters # 3. 합치기
    print(f'url: {url}')

    responseDecode=getRequestUrl(url) # 4. url 요청 후 응답객체 받기
    if responseDecode==None: return None # 5. 만약 응답객체가 None이면 None 반환
    else: return json.loads(responseDecode) # 6. 만약 응답객체가 존재하면 json형식을 파이썬 객체로 변환하는 함수
        # JSON=문자열타입
        # PY: json.loads() JSON형식 --> PY형식 반환 함수, json.dumps() PY형식 --> JSON형식 반환 함수
        # JS: JSON.parse() JSON형식 --> JS형식 반환 함수, JSON.stringify() JS형식 --> JSON형식 반환 함수

# [code4]
def getTourismStateService(start,end):
    jsonResult=[] # 수집한 데이터를 저장할 리스트 객체
    isDataEnd=0 # 데이터의 끝 확인하는 변수
    for index in range(start,end+1): # 시작연도 부터 마지막연도 까지 반복
        jsonData=getTourismStateItem(index,index)
        if jsonData!=None:
                print(f'jsonData: {jsonData}')
                # 만약에 지정한 날짜의 내용을
                # 내용물이 있으면
                data=jsonData['ChunmanFreeSuggestions']['row']
                print(data)
                for data2 in data:
                    sn=data2['SN']
                    title=data2['TITLE']
                    content=data2['CONTENT']
                    voteScore=data2['VOTE_SCORE']
                    regDate=data2['REG_DATE']
                    dic={'sn':sn,'title':title,'content':content,'voteScore':voteScore,'regDate':regDate}
                    jsonResult.append(dic)


    return jsonResult


# [code1]
def main():
    # 서비스 요청시 필요한 매개변수들을 입력받기
    start=int(input('시작행: ')) # 3. 데이터 수집 시작 연도
    end=int(input('종료행: ')) # 4. 마지막 데이터의 연도

    # 6. 서비스 요청후 응답 객체 받기
    jsonResult = []  # 1. 수집한 데이터를 저장할 리스트 객체
    jsonResult=getTourismStateService(start,end)
    print(f'jsonResult: {jsonResult}') # 확인

    # 7. 응답받은 py객체를 json으로 변환 후 파일처리
    with open(f'{start}-{end}.json',"w",encoding="utf-8") as file:
        jsonFile=json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        file.write(jsonFile)

if __name__=="__main__":
    main()




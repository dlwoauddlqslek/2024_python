# 1. BeautifulSoup 이용한 쿠우쿠우 전국 매장 정보 크롤링
# 2. 전국 쿠우쿠우 매장 정보(번호,매장명,연락처,주소,영업시간)
# 3. pandas 이용한 csv 파일 로 변환
# 4. 플라스크 이용한 쿠우쿠우 전국 매장 정보 반환 하는 HTTP 매핑 정의한다.
    # URL: ip주소:5000/qooqoo
    # (3) 생성된 csv 파일 읽어서(pandas DataFrame) json 형식으로 반환
'''
    정보의 html 식별자 확인
    1. 정보가 있는 위치 <tbody> 여러개 매장 정보
    2. <tr> 하나의 매장 정보 #홀수: pc #짝수: 모바일
    3. <td> 하나의 매장의 각 속성: <td> 1.번호 2.지점 3.연락처 4.주소 5.영업시간
    4. 데이터 상세 위치
        - 번호 <td>
        - 지점명 <td> -> <div> -> <a>
        - 연락처/주소/영업시간 데이터는 <td> -> <a>
'''
# 1. 모듈 가져오기
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json

# [1] 쿠우쿠우 매장 정보 크롤링 서비스
def qooqooInfo(result):
    for page in range(1,7):
        # 2. 지정한 url 호출해서 응답 받기
        url=f'http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}'
        response=urllib.request.urlopen(url)
        if response.getcode()==200:
            print('통신 성공')
            # 3. 통신 응답 결과를 읽어 와서 크롤링 파싱 준비
            htmlData = response.read()
            soup = BeautifulSoup(htmlData, 'html.parser')
            # print(soup)
            # 4. 분석한 HTML 식별자들을 파싱, find, findall, select, select_one
            # 4-1 테이블 전체 파싱
            tbody = soup.select('tbody')
            # print(tbody)
            rows = tbody[0].select('tr') # 4-2 테이블(전체매장) 마다 행(매장) 파싱
            for row in rows: # 4-3 행(매장) 마다
                # if len(row) >=13:
                tds = row.select('td') # 4-3 열(각매장정보) 파싱
                # 모바일 제외
                if len(tds) <= 1: # 만약에 열이 개수가 1개이면 모바일 이라고 가정해서 파싱 제외
                    continue # 가장 가까운 반복문으로 이동, 아래 코드는 실행되지 않는다.
                # 각 정보들 파싱, 공백 제거
                number = tds[0].string.strip();  # print(number)
                name1 = tds[1].select('a')[0].string.strip()
                name2 = tds[1].select('a')[1].string.strip()
                name = f'{name1}{name2}'
                phone = tds[2].text.strip();  # print(phone)
                address = tds[3].text.strip();  # print(address)
                time = tds[4].text.strip();  # print(time)

                # 5. 파싱한 정보를 리스트에 담기
                store = [number, name, phone, address, time]
                # print(store)
                result.append(store) # 리스트에 파싱한 리스트 담기 # 2차원 리스트(왜? df사용하기 위해서 2차원 리스트 구성)
        else:
            print('통신 실패')
    # 6. 리스트 반환
    return

# [2] 2차원 리스트를 csv 반환해주는 서비스
def list2d_to_csv():
    result=[]
    qooqooInfo(result)
    modify_result=[[field.replace(',','') for field in row]
                   for row in result
                   ]
    # print(modify_result)
    try:
        qooqoo_tbl=pd.DataFrame(modify_result,columns=('번호','매장명','연락처','주소','영업시간'))
        qooqoo_tbl.to_csv('qooqoo7.csv',encoding='utf-8',mode='w',index=True)
        return True
    except Exception as e:
        print(e)
        return False

# [3] csv 파일을 JSON 형식의 PY타입으로 가져오기, 가져올파일명
def read_csv_to_json(fileName):
    #1. 판다스를 이용한 csv를 데이터프레임으로 가져오기
    df = pd.read_csv(f'{fileName}.csv',encoding='utf-8',engine='python',index_col=0)
        # index_col=0: 판다스의 데이터프레임워크 형식 유지(테이블형식)
    # 2. 데이터프레임 객체를 JSON으로 가져오기
    jsonResult = df.to_json(orient='records', force_ascii=False)
        # to json(): 데이터프레임 객체 내 데이터를 JSON 반환함수
            # orient='records': 각 행마다 하나의 JSON 객체로 구성
            # force_ascii=Fale: 아스키 문자 사용 여부: True(아스키 사용), False(유니코드 utf-8)
    # 3. JSON 형식의 py타입(객체타입-리스트/딕셔너리)으로 변환
    result = json.loads(jsonResult) # import json 모듈 호출 # json.loads() 문자열타입(json형식) ---> py타입(json형식) 변환
    return result

if __name__=='__main__':
    list2d_to_csv()
    result2 = read_csv_to_json('qooqoo7') # csv파일을 json으로 가져오는 서비스 호출
    print(result2)


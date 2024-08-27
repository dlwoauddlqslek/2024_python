# 1. BeautifulSoup 이용한 쿠우쿠우 전국 매장 정보 크롤링
# 2. 전국 쿠우쿠우 매장 정보(번호,매장명,연락처,주소,영업시간)
# 3. pandas 이용한 csv 파일 로 변환
# 4. 플라스크 이용한 쿠우쿠우 전국 매장 정보 반환 하는 HTTP 매핑 정의한다.
    # URL: ip주소:5000/qooqoo
    # (3) 생성된 csv 파일 읽어서(pandas DataFrame) json 형식으로 반환
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

def qooqoo(result):
    for page in range(1,7):
        url=f'http://www.qooqoo.co.kr/bbs/board.php?bo_table=storeship&&page={page}'
        response=urllib.request.urlopen(url)
        htmlData=response.read()
        soup=BeautifulSoup(htmlData,'html.parser')
        #print(soup)
        tbody=soup.select('tbody')
        #print(tbody)
        for row in tbody[0].select('tr'):
            # if len(row) >=13:
            tds=row.select('td')
            if len( tds ) <= 1 :
                continue
            number=tds[0].string.strip(); #print(number)
            name1=tds[1].select('a')[0].string.strip()
            name2=tds[1].select('a')[1].string.strip()
            name=name1+name2
            phone=tds[2].text.strip(); #print(phone)
            address=tds[3].text.strip(); #print(address)
            time=tds[4].text.strip(); #print(time)
            store=[number,name,phone,address,time]
            result.append(store)
    return

def main():
    result=[]
    qooqoo(result)
    print(result)
    qooqoo_tbl=pd.DataFrame(result,columns=('번호','매장명','연락처','주소','영업시간'))
    qooqoo_tbl.to_csv('qooqoo3.csv',encoding='cp949',mode='w',index=False)
def load() :
    list = []
    f = open("qooqoo2.csv", "r")  # 파일 읽기 모드
    next(f)  # 첫번째 줄 스킵
    readlines = f.read()  # 파일 읽기
    rows = readlines.split("\n")  # 행 구분해서 저장
    for i in rows :
        if i :
            cols = i.split(',')             # 쉼표 구분해서 저장
            if len(cols)==6:
                dic = {'번호':cols[0],'매장명':cols[1],'연락처':cols[2],'주소':cols[3],'영업시간':cols[4]+cols[5]}
                list.append(dic)
                print(list)
            else:
                dic={'번호':cols[0],'매장명':cols[1],'연락처':cols[2],'주소':cols[3]+cols[4],'영업시간':cols[5]+cols[6]}
    return list

if __name__=='__main__':
    main()
    load()



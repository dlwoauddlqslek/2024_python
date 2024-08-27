# 1. 모듈
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime


def hollys_store(result):
    for page in range(1,51): # 1 ~ 50
        # 할리스 매장 정보 url
        url=f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}"
        response= urllib.request.urlopen(url)
        htmlData=response.read()
        soup=BeautifulSoup(htmlData,'html.parser')
        #print(soup)
        tbody=soup.select('tbody')
        #print(tbody)
        for row in tbody[0].select('tr'):
            if len(row) <=3:
                break
            #print(row)
            tds=row.select('td')
            store_sido=tds[0].string; #print(store_sido)
            store_name=tds[1].string; #print(store_name)
            store_address=tds[3].string; #print(store_address)
            store_phone=tds[5].string; #print(store_phone)
            store=[store_name,store_sido,store_address,store_phone] # 매장 정보 1개당 리스트 1개
            result.append(store) # 리스타 안에 리스트 요소 추가: 2차원 리스트 # [ [], [], [] ]
    return

def main():
    result = []  # 할리스 매장 딕셔너리를 여러개 저장하는 리스트 변수
    print('할리스 매장 크롤링중')
    hollys_store(result)
    #print(result)
    hollys_tbl=pd.DataFrame(result,columns=('store','sido-gu','address','phone'))
    hollys_tbl.to_csv('hollys.csv',encoding='cp949',mode='w',index=True)
    del result[:]

if __name__=='__main__':
    main()
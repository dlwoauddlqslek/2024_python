from bs4 import BeautifulSoup # 모듈 가져오기
import  urllib.request # 모듈 가져오기

# [실습1] http://quotes.toscrape.com
url="http://quotes.toscrape.com" # 크롤링할 url
response = urllib.request.urlopen(url) # 지정한 url 요청 후 응답 받기
htmlData = response.read() # 지정한 url
#print(htmlData)
soup = BeautifulSoup(htmlData,"html.parser") # 지정한 html문자열을 html 파싱객체 생성
#print(soup.prettify()) # 확인

# 특정 마크업/테크 파싱
quoteDivs=soup.select('.quote')
# print(quoteDivs)
for quote in quoteDivs:
    # 명언 문구만 추출
    print(quote.select_one('.text').string)
    # 각 명언 저자 추출
    print(quote.select('span')[1].select_one('small').string)
    # 각 명언 태그 목록 추출
    #print(quote.select('.tag'))
    for tag in quote.select('.tag'):
        print(tag.string,end='\t')
    print('\n')

# [실습2] https://v.daum.net/v/20240827074833139
url='https://v.daum.net/v/20240827074833139'
response = urllib.request.urlopen(url)
htmlData=response.read()
soup = BeautifulSoup(htmlData,"html.parser")
#print(soup)

# 파싱하기
ps=soup.select('p')

#for p in ps:
    #print(p.text)

# 기사 제목
#print(soup.select_one('.tit_view').string)
#print(soup.select_one('.news_view').text)

# [실습3]
    # https://search.naver.com/search.naver?query=%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8
url="https://search.naver.com/search.naver?query=%EB%B6%80%ED%8F%89%EA%B5%AC%EB%82%A0%EC%94%A8"
response=urllib.request.urlopen(url)
htmlData=response.read()
#print(htmlData)
soup=BeautifulSoup(htmlData,"html.parser")
# 온도 추출
print(soup.select_one('.temperature_text'))
# <div class="temperature_text"> <strong><span class="blind">현재 온도</span>27.0<span class="celsius">°</span></strong> </div>
print(soup.select_one('.temperature_text').text) # 현재 온도27.0°
print(soup.select_one('.summary_list').select('.sort')[1].text)
# 주제: 다음 경제 뉴스의 최신 10페이지 기사들 제목의 단어 빈도수 분석
import math
from collections import Counter
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import json
import re

#1. 데이터 준비
# url='https://news.daum.net/economic#1'
# response=urllib.request.urlopen(url)
# htmlData=response.read()
# soup=BeautifulSoup(htmlData,'html.parser')
textData=[]
for page in range(1,11):
    url=f'https://news.daum.net/breakingnews/economic?page={page}'
    response=urllib.request.urlopen(url)
    soup=BeautifulSoup(response,'html.parser')
    list=soup.select_one('.list_news2'); #print(list)
    for row in list.select('li'):
        list2 = row.select_one('.tit_thumb>a').string; #print(list2)
        textData.append(list2)

#2. 품사 태깅
message=''
for msg in textData:
    message+=re.sub(r'[^\w]',' ',msg)

from konlpy.tag import Okt
okt=Okt()
words=okt.nouns(message)
print(words)

#3. 분석(빈도수)

from collections import Counter
wordsCount=Counter(words)
bestWords=wordsCount.most_common(30)
wordsDict={}
for word,count in bestWords:
    if len(word)>1:
        wordsDict[word]=count
#4. 시각화(히스토그램,워드클라우드)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
wc=WordCloud('c:/windows/fonts/malgun.ttf',background_color='ivory').generate_from_frequencies(wordsDict)
plt.imshow(wc)
plt.show()

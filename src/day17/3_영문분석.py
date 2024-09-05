import pandas as pd
import glob
import re
from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

all_files=glob.glob('exportExcelData*.xls')
#print(all_files)

all_files_data=[]
for file in all_files:
    data_frame=pd.read_excel(file)
    all_files_data.append(data_frame)
#print(all_files_data)

all_files_data_concat=pd.concat(all_files_data,axis=0,ignore_index=True)
#print(all_files_data_concat)

all_title=all_files_data_concat['제목']
#print(all_title)

영문불용어목록=stopwords.words('english')
#print(영문불용어목록)
표제어객체=WordNetLemmatizer()

words=[]
for title in all_title:
    #print(title)
    EnWords=re.sub(r'[^a-zA-Z]'," ",str(title))

    EnWordsToken=word_tokenize(EnWords.lower())
    #print(EnWordsToken)

    EnWordsTokenStop=[w for w in EnWordsToken if w not in  ['artificial','intelligence']]
    EnWordsTokenStop = [w for w in EnWordsTokenStop if w not in 영문불용어목록]
    #print(EnWordsTokenStop)

    EnWordsTokenStopLemma=[]
    for w in EnWordsTokenStop:
        EnWordsTokenStopLemma.append(표제어객체.lemmatize(w))
    #print(EnWordsTokenStopLemma)
    words.append(EnWordsTokenStopLemma)
#print(words)

words2=reduce(lambda x,y:x+y,words)
#print(words2)

count=Counter(words2)
#print(count)

word_count=dict()

for tag, counts in count.most_common(50):
    if(len(tag)>1):
        word_count[tag]=counts
#print(word_count)

sorted_keys=sorted(word_count,key=word_count.get,reverse=True)
sorted_values=sorted(word_count.values(),reverse=True)
plt.bar(range(len(word_count)),sorted_values)
plt.xticks(range(len(word_count)),list(sorted_keys),rotation=90)
plt.show()

all_files_data_concat['doc_count']=0

summary_yaer=all_files_data_concat.groupby('출판일',as_index=False)['doc_count'].count()
#print(summary_yaer)

plt.xlabel('yaer')
plt.ylabel('doc_count')
plt.grid(True)
plt.plot(range(len(summary_yaer)),summary_yaer['doc_count'])
plt.xticks(range(len(summary_yaer)),[text for text in summary_yaer['출판일']],rotation=90)
plt.show()

stopwords=set(STOPWORDS)
wc=WordCloud(background_color='ivory',stopwords=stopwords,width=800,height=600)
cloud=wc.generate_from_frequencies(word_count)
plt.figure(figsize=(8,8))
plt.imshow(cloud)
plt.axis('off')
plt.show()
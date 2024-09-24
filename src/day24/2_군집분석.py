import pandas as pd
import math

# [1] 데이터 수집
df=pd.read_excel('Online_Retail.xlsx')
#print(df.head())

# [2] 데이터 준비 및 탐색
# 오류 데이터 정제
df=df[df['Quantity']>0]
df=df[df['UnitPrice']>0]
df=df[df['CustomerID'].notnull()]

# CustomerID 자료형을 정수형으로 변환
df['CustomerID']=df['CustomerID'].astype(int)
print(df.info())
print(df.isnull().sum())
print(df.shape)

# 중복 레코드 제거
df.drop_duplicates(inplace=True)
print(df.shape)

print(pd.DataFrame([{'Product':len(df['StockCode'].value_counts()),'Transaction':len(df['InvoiceNo'].value_counts()),'Customer':len(df['CustomerID'].value_counts())}],columns=['Product','Transaction','Customer'],index=['counts']))
print(df['Country'].value_counts())

# 주문 금액 컬럼 추가
df['SaleAmount']=df['UnitPrice']*df['Quantity']
print(df.head())

aggregations={
    'InvoiceNo':'count',
    'SaleAmount':'sum',
    'InvoiceDate':'max'
}

customer_df=df.groupby('CustomerID').agg(aggregations)
customer_df=customer_df.reset_index()
print(customer_df.head())

customer_df=customer_df.rename(columns={'InvoiceNo':'Freq','InvoiceDate':'ElapsedDays'})
print(customer_df.head())

import datetime

customer_df['ElapsedDays']=datetime.datetime(2011,12,10)-customer_df['ElapsedDays']

customer_df['ElapsedDays']=customer_df['ElapsedDays'].apply(lambda x:x.days+1)
print(customer_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

fig,ax=plt.subplots()
ax.boxplot([customer_df['Freq'],customer_df['SaleAmount'],customer_df['ElapsedDays']],sym='bo')
plt.xticks([1,2,3],['Freq','SaleAmount','ElapsedDays'])
plt.show()

import numpy as np
customer_df['Freq_log']=np.log1p(customer_df['Freq'])
customer_df['SaleAmount_log']=np.log1p(customer_df['SaleAmount'])
customer_df['ElapsedDays_log']=np.log1p(customer_df['ElapsedDays'])
print(customer_df.head())

fig,ax=plt.subplots()
ax.boxplot([customer_df['Freq_log'],customer_df['SaleAmount_log'],customer_df['ElapsedDays_log']],sym='bo')
plt.xticks([1,2,3],['Freq_log','SaleAmount_log','ElapsedDays_log'])
plt.show()

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score,silhouette_samples
x_features=customer_df[['Freq_log','SaleAmount_log','ElapsedDays_log']].values
from sklearn.preprocessing import StandardScaler
x_features_scaled=StandardScaler().fit_transform(x_features)

distortions=[]

for i in range(1,11):
    kmeans_i=KMeans(n_clusters=i,random_state=0) # 모델 생성
    kmeans_i.fit(x_features_scaled)              # 모델 훈련
    distortions.append(kmeans_i.inertia_)

plt.plot(range(1,11),distortions,marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

kmeans=KMeans(n_clusters=3,random_state=0) # 모델 생성
# 모델 학습과 결과 예측(클러스터 레이블 생성)
y_labels=kmeans.fit_predict(x_features_scaled)
customer_df['ClusterLabel']=y_labels
print(customer_df.head())

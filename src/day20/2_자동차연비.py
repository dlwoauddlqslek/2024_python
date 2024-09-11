import numpy as np
import pandas as pd
data_df=pd.read_csv('auto_mpg.csv',header=0,engine='python')
#print(f'데이터셋 크기: {data_df.shape}')
#print(data_df.head())
data_df=data_df.drop(['car_name','origin','horsepower'],axis=1,inplace=False)
#print(data_df.head())
#print(f'데이터셋 크기: {data_df.shape}')
#data_df.info()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

# X, Y 분할하기
Y=data_df['mpg']
X=data_df.drop(['mpg'],axis=1,inplace=False)

# 훈련용 데이터와 평가용 데이터 분할하기
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)

# 선형 회귀 분석: 모델 생성
lr=LinearRegression()

# 선형 회귀 분석: 모델 훈련
lr.fit(X_train,Y_train)

# 선형 회귀 분석: 평가 데이터에 대한 예측 수행 -> 예측 결과 Y_predict 구하기
Y_predict = lr.predict(X_test)

mse=mean_squared_error(Y_test,Y_predict)
rmse=np.sqrt(mse)
print(f'mse: {mse}, rmse: {rmse}')
print(f'r^2(variance score): {r2_score(Y_test,Y_predict)}')

print(f'Y 절편 값: {np.round(lr.intercept_,2)}')
print(f'회귀 계수 값: {np.round(lr.coef_,2)}')

coef=pd.Series(data=np.round(lr.coef_,2),index=X.columns)
coef.sort_values(ascending=False)
print(coef)

import matplotlib.pyplot as plt
import seaborn as sns

fig,axs=plt.subplots(figsize=(16,16), ncols=3, nrows=2)
x_features=['model_year','acceleration','displacement','weight','cylinders']
plot_color=['r','b','y','g','r']
for i,feature in enumerate(x_features):
    row=int(i/3)
    col=i%3
    sns.regplot(x=feature,y='mpg',data=data_df,ax=axs[row][col],color=plot_color[i])
plt.show()

print('연비를 예측하고 싶은 차의 정보를 입력해주세요')
cylinder=int(input("cylinder: "))
displacement=int(input("displacement: "))
weight=int(input("weight: "))
acceleration=int(input("acceleration: "))
model_year=int(input("model_year: "))

mpg_predict=lr.predict([[cylinder,displacement,weight,acceleration,model_year]])
print(f'이 자동차의 예상 연비(MPG)는 {mpg_predict}입니다.')
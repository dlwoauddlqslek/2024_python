import pandas as pd
import numpy as np
#[1] 데이터 수집, 준비 및 탐색

# 보스턴 주택 데이터 가져오기 # sklearn 1.2
data_url = "http://lib.stat.cmu.edu/datasets/boston" # 보스턴 주택 정보가 있는 url
raw_df = pd.read_csv(data_url, sep="\\s+", skiprows=22, header=None)
    # 지정한 url 에서 데이터를 데이터프레임으로 가져오기
    # sep="\s+": 데이터간의 공백으로 구분된 csv
    # skiprows=22: 위에서부터 22행까지 생략
    # header=None: 헤더가 없음
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

#print(data.shape) # 주택관련변수들(독립변수,피처)
#print(target.shape) # 주택가격(종속변수, 타겟변수)
# 독립변수의 이름
feature_names = ['CRIM', 'ZN', 'INDUS','CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
# 독립변수 데이터와 독립변수의 이름으로 데이터프레임 생성
boston_df=pd.DataFrame(data,columns=feature_names)
# 데이터프레임의 주택가격 열 추가
boston_df['PRICE']=target
#print(boston_df.head())
#print('보스턴 주택 가격 데이터셋 크기: ',boston_df.shape)
#boston_df.info()

#[2] 분석 모델 구축

# 1. 타겟과 피처 분할하기
Y=boston_df['PRICE'] # 종속변수, 타겟 # 주택가격
X=boston_df.drop(['PRICE'],axis=1,inplace=False) # 독립변수, 피처 # 주택가격 외 정보
# 2. 훈련용과 평가용 분할하기
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=156)
# 훈련용독립변수, 테스트용독립변수, 훈련용종속변수, 테스트용종속변수 = train_test_split(독립변수, 종속변수, test_size=분할비율, random_state=난수생성시드)
# test_size=0.3 # 훈련용 70%, 테스트용 30% 분할
#print(x_train) # (354,13) 70%
#print(x_test)   # (152,13) 30%

# 3. 선형 회귀 분석 모델 생성
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
lr=LinearRegression()

# 4. 모델 훈련
lr.fit(x_train,y_train) # 훈련용 데이터를 이용한 모델 훈련


# 5. 테스트용으로 예측하기 # 테스트용에 있는 주택 정보를 이용한 주택 가격 예측하기
y_predict=lr.predict(x_test)

# 6. 평가지표 확인하기( MSE, RMSE, 결정계수, Y절편, 회귀계수)
# y_test # 동일한 피처 정보를 가진 실제 주택가격
# y_predict # 동일한 피처 정보를 가진 예측한 주택가격

mse=mean_squared_error(y_test,y_predict)
rmse=np.sqrt(mse)
print(f'MSE:{mse:.3f}, RMSE:{rmse:.3f}')
print(f'R^2(Variance score): {r2_score(y_test,y_predict):.3f}')
print('Y 절편 값: ',lr.intercept_)
print('회귀 계수 값: ',np.round(lr.coef_,1)) # 기울기 값
coef=pd.Series(data=np.round(lr.coef_,2),index=X.columns)
coef.sort_values(ascending=False)
print(coef)

# [3] 결과 시각화
import matplotlib.pyplot as plt
import seaborn as sns # 회귀분석 관련 차트 구성

sns.regplot(x='CRIM',y='PRICE',data=boston_df)
    # CRIM: 지역별 범죄 발생률 # PRICE: 주택 가격 # 범죄 발생률에 따른 주택 가격을 시각화
plt.show()
    # - y절편: 독립변수가 0일 때 종속변수의 값
    # - 회귀계수: 독립변수 1 증가 할 때 마다 종속변수의 증감 단위 # 기울기
    # - 신뢰구간: 좁으면 예측이 안정적이고 관계가 명확하다 해석, 넓다면 예측이 불안정하고 관계가 불명확하다.
fig,axs=plt.subplots(figsize=(16,16),ncols=3,nrows=5)
for i,feature in enumerate(feature_names): # for 요소인덱스, 요소값 in enumerate(리스트):
    print(i)
    print(feature)
    row=int(i/3) # 몫 # 3개씩 행이 바뀔 때 마다 몫의 값이 바뀜
    col=i%3 # 나머지
    sns.regplot(x=feature,y='PRICE',data=boston_df,ax=axs[row][col])
plt.show()
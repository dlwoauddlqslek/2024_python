import matplotlib.pyplot as plt
import pandas as pd

try:
    df2=pd.read_csv('samsung.csv',engine='c') #utf-8 기본값으로 인코딩
except Exception as e: # utf-8 인코딩 오류이면 cp949 인코딩하기
    df2 = pd.read_csv('samsung.csv', encoding='cp949', engine='c')
#print(df2)
# 주의할 점: 파일들의 인코딩 방식(utf-8, cp949, ISO-8859 등등)

# 데이터프레임의 특정 열 호출 # 데이터프레임['열이름']
#print(df2['일자'])

x=df2['일자'].tolist();print(x) # 데이터프레임 일자(열) 를 x축
y=df2['종가'].tolist();print(y) # 데이터프레임 종가(열) 를 y축
x=list(reversed(x)); print(x)
y=list(reversed(y)); print(y)
# 시각화
plt.plot(x,y)
plt.xlabel('date')
plt.ylabel('closing price')
plt.show()

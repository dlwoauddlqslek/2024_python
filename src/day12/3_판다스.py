# p124 연습문제
import matplotlib.pyplot as plt
import pandas as pd

df=pd.DataFrame([[500,450,520,610],[690,700,820,900],[1100,1030,1200,1380],[1500,1650,1700,1850],[1990,2020,2300,2420],[1020,1600,2200,2550]],index=['2015','2016','2017','2018','2019','2020'],columns=['1분기','2분기','3분기','4분기']);
print(df)
df.to_csv('sales.csv',encoding='utf-8',header='False')

x=['first','second','third','fourth']
y1=[500,450,520,610]
y2=[690,700,820,900]
y3=[1100,1030,1200,1380]
y4=[1500,1650,1700,1850]
y5=[1990,2020,2300,2420]
y6=[1020,1600,2200,2550]
plt.plot(x,y1, label='2015')
plt.plot(x,y2, label='2016')
plt.plot(x,y3, label='2017')
plt.plot(x,y4, label='2018')
plt.plot(x,y5, label='2019')
plt.plot(x,y6, label='2020')
plt.title('2015~2020 Quarterly sales')
plt.xlabel('Quarters')
plt.ylabel('Sales')
plt.legend()
plt.show()





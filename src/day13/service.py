import pandas as pd
import json

house2022=pd.read_csv('아파트2022.csv',encoding='cp949',header=15);#print(house2022)
house2023=pd.read_csv('아파트2023.csv',encoding='cp949',header=15);#print(house2023)
house2024=pd.read_csv('아파트2024.csv',encoding='cp949',header=15);#print(house2024)
#print(house2022.shape);print(house2023.shape);print(house2024.shape)# 17805,10368,8858
house=pd.concat([house2022,house2023,house2024]);print(house)

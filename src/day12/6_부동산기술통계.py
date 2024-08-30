import pandas as pd
import json
def statistics():
    house_pd=pd.read_csv('아파트.csv',encoding='cp949',header=0);print(house_pd)
    print(house_pd.head())
    print(( house_pd.describe()))
    print((house_pd.describe().index))
    jsonResult=house_pd.describe().to_json(orient='records',force_ascii=False)
    result=json.loads(jsonResult); print(result)
    return result

# 전체 데이터프레임 객체 생성
df=pd.DataFrame() # 빈 데이터프레임
for year in range(2022,2025): # 2022~2024
    # 각 년도의 csv 파일을 반복문 통해 여러번 호출한다.
    df2=pd.read_csv(f'아파트{year}.csv',encoding='cp949',header=15) # encoding='utf-8' : 기본값(생략시)
    print(df2.shape) # .shape: 레코드수, 열개수 확인
    df=pd.concat([df,df2]) # 기존 데이터프레임에 새로운 데이터프레임 연결/연장
print(df.shape) # (37031,21)
#print(house2022.shape);print(house2023.shape);print(house2024.shape)# 17805,10368,8858


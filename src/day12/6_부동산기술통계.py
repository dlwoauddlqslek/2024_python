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

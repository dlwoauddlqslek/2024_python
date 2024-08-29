import pandas as pd
import json
def statistics():
    house_pd=pd.read_csv('아파트.csv',encoding='cp949',header=0);print(house_pd)
    house_pd.columns=house_pd.columns.str.replace('(','_')
    house_pd.columns = house_pd.columns.str.replace(' ', '_')
    house_pd.columns = house_pd.columns.str.replace(')', '')
    house_pd.columns = house_pd.columns.str.replace('㎡', '')

    print(house_pd.head())
    print(( house_pd.describe()))
    print((house_pd.describe().index))
    index=house_pd.describe().index.tolist(); print(index)
    jsonIndex=[]
    for value in index:
        jsonIndex.append({'index':value})
    print(jsonIndex)
    jsonResult=house_pd.describe().to_json(orient='records',force_ascii=False)
    result=json.loads(jsonResult); print(result)
    for i in range(0, 8):
        result[i].update(jsonIndex[i])
    print(result)
    return result

# def division():
#     house_pd=pd.read_csv('아파트.csv',encoding='cp949',header=0);
#     div= house_pd.groupby('전월세구분').describe()['전용면적(㎡)'].to_list()
#     print(div)


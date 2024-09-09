# 주제: 커피 매장의 주소를 이용한 지도에 마커 표시하기
# 실습파일: CoffeeBean.csv
import json
# 1. 데이터준비
import pandas as pd
df = pd.read_csv('CoffeeBean.csv',encoding='cp949',index_col=0)
#print(df)

# 2. 데이터 가공

# Flask 모듈 가져오기
from flask import Flask

# Flask 객체 생성
app = Flask( __name__ )

from flask_cors import CORS
CORS( app ) # 모든 경로에 대해 CORS 허용

@app.route( "/" )
def index() :
    # df 객체를 json 변환
    jsonData=df.to_json(orient='records',force_ascii=False)
    # json 형식을 py형식으로 변환
    result=json.loads(jsonData)
    return result

if __name__ == "__main__" :
    app.run( )

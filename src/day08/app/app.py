# day08 > app > app.py
from flask import Flask
app = Flask( __name__ )
from flask_cors import CORS #(3) CORS 모듈 가져오기
CORS( app ) # (4) 모든 HTTP 경로의 CORS 허용
# [모듈] controller.py 의 매핑 함수들 가져오기
from controller import *

if __name__ == "__main__" :
    app.run()
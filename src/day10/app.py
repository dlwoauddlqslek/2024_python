from flask import Flask # 1. 플라스크 모듈 가져오기
from flask_cors import CORS # 3. CORS 모듈 가져오기
app = Flask(__name__)   # 2. 플라스크 객체 생성
CORS(app)   # 4. 모든 HTTP 경로의 CORS 허용.
# controller 모듈 가져오기
from controller import *


if __name__ == "__main__" : # 6. Flask 실행
    app.run(host='0.0.0.0' , debug=True)
    # http://127.0.0.1:5000
    # http://localhost:5000
    # http://192.168.30.21:5000
# 서버 재실행시 직접 현재 실행 중지하기
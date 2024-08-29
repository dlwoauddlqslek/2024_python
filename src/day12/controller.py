# [1] 플라스크 객체 가져오기
from app import app
# [2] (우리가 만든) 서비스 모듈 가져오기
from service import *
# app.run 코드 위에 HTTP 매핑 주소 정의
@app.route('/stati', methods=['get'])
def apart():
    #(1) 만약 크롤링 된 csv 파일이 없거나 최신화 하고 싶을 대
    result=statistics()
    return result
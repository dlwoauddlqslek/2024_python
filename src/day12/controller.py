# [1] 플라스크 객체 가져오기
from collections import OrderedDict


from flask import jsonify
from app import app
# [2] (우리가 만든) 서비스 모듈 가져오기
from service import *
# app.run 코드 위에 HTTP 매핑 주소 정의
@app.route('/stati', methods=['get'])
def apart():

    result=statistics()
    return result

@app.route('/division', methods=['get'])
def individual():

    result=division()
    print(result)
    return result

@app.route('/dupl', methods=['get'])
def dupli():

    result=dupl()
    return result

@app.route('/most', methods=['get'])
def most5():

    result=most()
    print(result)
    return  jsonify( result)


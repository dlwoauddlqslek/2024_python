from app import app # Flask 객체 호출
from service import *

@app.route("/", methods=["GET"])
def index() :
    data = load()
    return data

@app.route("/2", methods=["GET"])
def index2() :
    data = load2()
    return data
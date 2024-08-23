from app import app # Flask 객체 호출
from service import *

@app.route("/", methods=["GET"])
def index() :
    data = load()
    data = list( map( lambda o : o.__dict__ , data ) )
    return data

@app.route("/2", methods=["GET"])
def index2() :
    data = load2()
    data = list( map( lambda o : o.__dict__ , data ) )
    return data
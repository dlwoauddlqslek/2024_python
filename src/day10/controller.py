from app import app # Flask 객체 호출
from service import *

@app.route("/qooqoo", methods=["GET"])
def index() :
    data = load()
    data = list( map( lambda o : o.__dict__ , data ) )
    return data


from app import app # Flask 객체 호출

@app.route("/qooqoo", methods=["GET"])
def load() :
    list = []
    f = open("qooqoo2.csv", "r")  # 파일 읽기 모드
    next(f)  # 첫번째 줄 스킵
    readlines = f.read()  # 파일 읽기
    rows = readlines.split("\n")  # 행 구분해서 저장
    for i in rows :
        if i :
            cols = i.split(',')             # 쉼표 구분해서 저장
            if len(cols)==6:
                dic = {'번호':cols[0],'매장명':cols[1],'연락처':cols[2],'주소':cols[3],'영업시간':cols[4]+cols[5]}
                list.append(dic)
                print(list)
    return list


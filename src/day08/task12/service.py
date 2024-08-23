from apart import apartment
def load() :
    list = []
    f = open("아파트(매매)_실거래가_20240823161105.csv", "r")  # 파일 읽기 모드
    next(f)  # 첫번째 줄 스킵
    readlines = f.read()  # 파일 읽기
    rows = readlines.split("\n")  # 행 구분해서 저장
    for i in rows :
        if i :
            cols = i.split(',')             # 쉼표 구분해서 저장
            if len(cols)==21:
                dic = {'시군구':cols[1],'단지명':cols[5],'전용면적':cols[6],'계약년월':cols[7],'계약일':cols[8],'거래금액':int(eval(cols[9]+cols[10])),'층':cols[12]}
                list.append(dic)
    return list



def load2() :
    list2 = []
    list = load()
    maxPrice=max(list,key=lambda x:x['거래금액'])
    minPrice=min(list,key=lambda x:x['거래금액'])
    list2.append(maxPrice)
    list2.append(minPrice)
    print(list2)
    return list2

def load3():
    list3=[]
    list=load()



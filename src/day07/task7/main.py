# 다른 파일의 클래스 가져오기
from Info import Info # Info 클래스 가져오기
names=[]
def nameCreate():
    global names # 함수안에서 전역변수를 호출하는 방법, global 전역변수명
    name=input('이름: ')
    age=input('나이: ')
    new=Info(name,age); print(new.age+new.name)
    names.append(new)
    return
def nameRead():
    for info in names:
        print(f'이름: {info.name} 나이: {info.age}')
    return
def nameUpdate():
    oldName = input("수정할 이름: ")
    for name in names:
        if name.name == oldName:
            newName = input("새로운 이름: ")
            name.name = newName
            newAge=input("새로운 나이: ")
            name.age=newAge
            return
    return
def nameDelete():
    deleteName = input("삭제할 이름: ")
    for name in names:
        if name.name == deleteName:
            names.remove(name)
            return  # 1개만 삭제하기 위해서는 삭제후 return
    return

# 해당 파일을 다른 파일에서 호출했을 때 호출 되지 않는 구역
    # 해당 파일을 직접 실행할대는 실행되는 구역
    # 해당 파일을 다른 파일에서 호출 할때 실행되지 않는 구역[모듈]
if __name__=="__main__":
    while True: # 무한루프
        ch=input("1.create 2.read 3.update 4.delete: ")
        if ch=='1':
            nameCreate()
        elif ch=='2':
            nameRead()
        elif ch=='3':
            nameUpdate()
        elif ch=='4':
            nameDelete()
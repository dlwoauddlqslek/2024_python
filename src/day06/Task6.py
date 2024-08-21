
# 객체/리스트 활용 , p.190 ~ p.207
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 한명의 이름과 나이를 입력받아 저장합니다.
#          2. 저장된 여러명의 이름, 나이를 모두 출력
#          3. 수정할 이름을 입력받아 존재하면 새로운 이름,나이를 입력받고 수정합니다.
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.
# [조건4] : 프로그램이 종료되고 다시 실행되더라도 기존의 names 데이터가 유지되도록 파일처리
names=[]
class Info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
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

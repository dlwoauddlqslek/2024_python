# 문자열 활용, p.50 ~ p.76
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여러명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.
names="" # 여러개 name들을 저장하는 문자열 변수


def nameCreate():
    global names
    name=input("이름을 입력하세요: ")
    print(name)
    if names:
        names+=" "
    names+=name
    return
def nameRead():
    print(names)
    return
def nameUpdate():
    global names
    old=input("수정할 이름을 입력하세요: ")
    new=input("새로운 이름을 입력하세요: ")
    names=names.replace(old,new)
    return
def nameDelete():
    global names
    delete=input("삭제할 이름을 입력하세요: ")

    if names.count(delete)==1:
        names=names.replace(delete,"")
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
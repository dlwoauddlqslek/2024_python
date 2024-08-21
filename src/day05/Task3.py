# 튜플 활용 , p.89 ~ p.92
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여러명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.

# 튜플이란? 리스트와 비슷, 차이점: 요소의 삽입/삭제가 불가능
    # 튜플은 불변성을 가진다. 리터럴과 같다.
    # a=3+2,
    #='py'+'3'

names=('이일','이이','이삼','이사') # 여러개 name들을 저장하는 문자열 변수

def nameCreate():
    global names # 함수안에서 전역변수를 호출하는 방법, global 전역변수명
    #lst=list(names)
    name=input('이름: ')
    names+=(name,)
    #lst.append(name)
    #names=tuple(lst)
    print(names)
    return
def nameRead():
    for name in names:
        print(f'이름: {name}')
    return
def nameUpdate():
    global names
    newNames=()
    oldName=input("수정할 이름: ")
    for name in names:
        if name!=oldName:
            newNames+=(name,)
        else:
            newName=input("새로운 이름: ")
            newNames+=(newName,)
    names=newNames
    return
def nameDelete():
    global names
    deleteName=input("삭제할 이름: ")
    if names.count(deleteName)==0: return
    else:
        newNames = ()       # 새로운 튜플
        for name in names:  # 튜플에서 하나씩 요소를 반복
            if name==deleteName: # 삭제할 요소값은 생략
                continue
            else:
                newNames+=(name,) # 새로운 튜플에 기존값 누적
        names=newNames
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
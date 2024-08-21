# 문자열 활용, p.50 ~ p.76
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여러명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.

names="유재석,강호동,신동엽" # 여러개 name들을 저장하는 문자열 변수
    # 하나의 변수에 여러개의 이름을 저장하는 방법.
    # 변수란? 하나의 자료를 저장하는 메모리 공간
    # 하나의 자료에 여러가지 속성을 담는 방법: 1.객체 2.문자열(JSON 형식, CSV형식) 3.리스트 4.튜플
        # 타입(자료 분류) vs 형식(자료 모양)
        # "10" : 문자열타입, 숫자형식, 10 : 정수타입, 숫자형식
        # "{key:value}" : 문자열타입, JSON형식 # {key:value} : JSON/딕셔너리 타입, JSON/딕셔너리 형식
    # CSV란? 몇가지 필드를 쉼표(,)로 구분한 텍스트
def nameCreate():
    global names # 함수안에서 전역변수를 호출하는 방법, global 전역변수명
    newName=input("newName: ") # 저장할 새로운 이름 입력받기
    # 첫번째 이름이면 가장앞에 ,(쉼표)가 없어도 된다.
        # 삼항연산자: 참 if 조건문 else 거짓
        # 문자열.count(문자) : 문자열내 문자 개수 반환
    names +=f'{'' if names.count(',')==0 else','}{newName}' # ,(쉼표) 여러개 이름중에 이름을 구분하는 구분문자(CSV형식)
    return
def nameRead():
    # for 반복변수 in 리스트명: # 리스트내 요소 하나씩 반복변수에 대입, js: 리스트명.forEach(반복변수=>{})
    # for 반복변수 in 문자열: # 문자열내 문자 하나씩 반복변수에 대입
    for name in names.split(','):
        print(f'name : {name}') # f'문자열{코드}문자열' # js:'문자열${코드}문자열'
    return
def nameUpdate():
    global names
    # 문자열(불변성 특징) , # 부분수정x # 문자열내 중간에 다른 문자열로 변경
    # 만약 동일한 문자를 찾는다면 새로운 문자로 변경
    oldName=input('oldName : ')
    if names.find(oldName)==-1:
        return
    else:
        newName=input('newName : ')
        #names=names.replace(oldName,newName)
        newNames=""
        for name in names.split(','): # 이름 하나씩 반복
            if name==oldName : # 수정할 이름과 같으면
                newNames+=f'{newName}' # 새로운이름
            else:
                newNames+=f'{''if newNames==""else','}{name}' # 기존이름
        names=newNames # 새로 구성한 이름명단을 전역변수에 대입
    return
def nameDelete():
    global names
    # 만약 동일한 문자를 찾는다면 ''로 변경
    deleteName=input("deleteName: ")
    if names.find(deleteName)==-1:
        return
    else: # 존재하면
        # 문자열.replace(기존문자, 새로운문자) # 문자열내 기존문자가 존재하면 새로운문자로 치환해서 반환
        # names=names.replace(f',{deleteName}',"")
        # replace 이름 단위가 아닌 문자 단위 수정이 되므로 문제가 발생할 수도 있다.
        newNames=""
        for name in names.split(','):
            if name==deleteName:
                continue # 가장 가까운 반복문으로 이동
            else :
                print(name)
                newNames+=f'{''if newNames==""else','}{name}'
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
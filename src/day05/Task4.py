# 딕셔너리/리스트 활용 , p.93 ~ p.101
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여러명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.
    # 딕셔너리란? {}안에 key: value 쌍으로 저장하는 자료, JSON과 비슷하다.
    # 리스트[] 안에 여러개 딕셔너리 {} 저장된 설계
names=[{'이름':'이일'},{'이름':'이이'},{'이름':'이삼'},{'이름':'이사'}] # 여러개 name들을 저장하는 문자열 변수

def nameCreate():
    global names # 함수안에서 전역변수를 호출하는 방법, global 전역변수명
    print(names)
    name=input('이름: ')
    newName={'이름':name} # 딕셔너리 구성
    names.append(newName)   # 딕셔너리를 리스트에 삽입
    print(names)
    return
def nameRead():
    for name in names: # 리스트내 딕셔너리 하나씩 호출
        print(f'이름: {name['이름']}')  # 딕셔너리변수명[key] 또는 딕셔너리변수명.get(key)
    return
def nameUpdate():
    global names
    oldName=input("수정할 이름: ")
    for name in names:
        if name.get('이름')==oldName:
            newName=input("새로운 이름: ")
            name['이름']=newName # 해당 딕셔너리의 속성 값 수정
            return
    return
def nameDelete():
    global names
    deleteName=input("삭제할 이름: ")
    for name in names:
        if name.get('이름')==deleteName:
            names.remove(name) # 리스트변수명.remove(삭제할딕셔너리)
            return # 1개만 삭제하기 위해서는 삭제후 return
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
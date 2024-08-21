# 리스트 활용 , p.77 ~ p.88
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 이름을 입력받아 여러명의 이름을 저장
#          2. 저장된 여러명의 이름을 모두 출력
#          3. 수정할 이름과 새로운 이름을 입력받아 수정
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.

names=['이일','이이','이삼','이사']
def nameCreate():
    global names
    name=input('이름: ')
    names.append(name) # 리스트변수.append(새로운값) : 리스트내 마지막 요소 뒤에 새로운값 요소 추가
    print(names)
    return
def nameRead():
    for name in names[0:]:
        print(f'이름: {name}')
    return
def nameUpdate():
    global names
    #i=0
    oldName=input('수정할 이름: ')
    # 수정할 이름이 존재하지 않으면
    if names.count(oldName)==0:return
    else: #존재하면
        # 수정할 이름의 인덱스 찾기,
        # 리스트변수명.index(찾을값) : 리스트내 찾을값이 존재하면 인덱스 반환
        index=names.index(oldName)
        newName=input('새로운 이름: ') # 새로운 이름
        names[index]=newName        # 찾은 인덱스에 새로운 값 대입
    #for name in names[0:]:
    #    print(name)
    #    if name!=oldName:
    #        i+=1
    #        continue
    #    else:
    #        newName = input('새로운 이름: ')
    #        names[i]=newName
    #        return
    return
def nameDelete():
    global names
    #i=0
    deleteName=input('삭제할 이름: ')
    if names.count(deleteName)==0:return
    names.remove(deleteName) # 리스트변수명.remove()
    #for name in names[0:]:
    #    print(name)
    #    if name!=deleteName:
    #        i+=1
    #        continue
    #    else:
    #        del names[i]
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
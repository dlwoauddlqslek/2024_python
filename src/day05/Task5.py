# 딕셔너리/리스트 활용 , p.93 ~ p.101
# [조건1] : 각 함수들을 구현해서 프로그램 완성
# [조건2] : 1. 한명의 이름과 나이를 입력받아 저장합니다.
#          2. 저장된 여러명의 이름, 나이를 모두 출력
#          3. 수정할 이름을 입력받아 존재하면 새로운 이름,나이를 입력받고 수정합니다.
#          4. 삭제할 이름을 입력받아 존재하면 삭제
# [조건3] : names 변수 외 추가적인 전역 변수 생성 불가능.
# [조건4] : 프로그램이 종료되고 다시 실행되더라도 기존의 names 데이터가 유지되도록 파일처리

names=[] # 여러개 name들을 저장하는 문자열 변수

def dataLoad(): # 파일내 데이터를 불러오기 , while True 위에서 실행, 프로그램 시작시 실행
    global names
    f=open('names.txt','r',encoding='utf-8') # 파일 읽기모드로 객체 반환
    info=f.read()   # 파일내 데이터 전체읽어오기, 파일객체.read()
    print(info)
    # 딕셔너리를 만들고 리스트에 담기
    lines=info.split('\n')  # 줄마다(요소)
    for line in lines[:len(lines)-1]: # 읽어온 파일 내용을 \n 분해해서 한줄씩 반복처리, \n으로 객체 구분, 마지막줄 제외
        dic={'이름':line.split(',')[0],'나이':line.split(',')[1]} # 해당 줄에,로 분해 [0]이름[1]나이
        names.append(dic) # 리스트에 저장
    f.close()

def dataSave(): # 데이터를 파일내 저장하기, create,update,delete에서 사용
    global names
    f=open('names.txt','w',encoding='utf-8') # 파일 쓰기모드로 객체 반환
    # 파이썬의 딕셔너리 -> 문자열 만들고 파일 쓰기
    outstr=""   # 파일 작성할 문자열 변수
    for info in names:
        outstr+=f'{info['이름']},{info['나이']}\n' # 딕셔너리를 csv혁식의 문자열로 변환
    f.write(outstr) # 파일객체 이용한 데이터 쓰기, 파일객체.write(데이터)
    f.close()   # 파일객체 닫기, 파일객체.close()
def nameCreate():
    global names # 함수안에서 전역변수를 호출하는 방법, global 전역변수명
    name=input('이름: ')
    age=input('나이: ')
    new={'이름':name,'나이':age}
    names.append(new)
    dataSave()
    return
def nameRead():
    print(names)
    for info in names:
        print(f'이름: {info['이름']} 나이: {info['나이']}')
    return
def nameUpdate():
    global names
    oldName = input("수정할 이름: ")
    for name in names:
        if name.get('이름') == oldName:
            newName = input("새로운 이름: ")
            name['이름'] = newName  # 해당 딕셔너리의 속성 값 수정
            newAge=input("새로운 나이: ")
            name['나이']=newAge
            dataSave()
            return
    dataSave()
    return
def nameDelete():
    global names
    deleteName = input("삭제할 이름: ")
    for name in names:
        if name.get('이름') == deleteName:
            names.remove(name)  # 리스트변수명.remove(삭제할딕셔너리)
            dataSave()
            return  # 1개만 삭제하기 위해서는 삭제후 return
    return

dataLoad()
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
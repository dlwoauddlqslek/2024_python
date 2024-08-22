from User import User



def dataSave(names): # 데이터를 파일내 저장하기, create,update,delete에서 사용
    f=open('names.txt','w',encoding='utf-8') # 파일 쓰기모드로 객체 반환
    # 파이썬의 딕셔너리 -> 문자열 만들고 파일 쓰기
    outstr=""   # 파일 작성할 문자열 변수
    for info in names:
        outstr+=f'{info.name},{info.age}\n' # csv혁식의 문자열로 변환
    f.write(outstr) # 파일객체 이용한 데이터 쓰기, 파일객체.write(데이터)
    f.close()   # 파일객체 닫기, 파일객체.close()

def dataLoad(): # 파일내 데이터를 불러오기 , while True 위에서 실행, 프로그램 시작시 실행
    try: #예외처리 # 예외가 발생 할것 같은 코드
        f=open('names.txt','r',encoding='utf-8') # 파일 읽기모드로 객체 반환
        names=[]
        info=f.read()   # 파일내 데이터 전체읽어오기, 파일객체.read()
        # 딕셔너리를 만들고 리스트에 담기
        lines=info.split('\n')  # 줄마다(요소)
        for line in lines[:len(lines)-1]: # 읽어온 파일 내용을 \n 분해해서 한줄씩 반복처리, \n으로 객체 구분, 마지막줄 제외
            if line: # 만약 데이터가 존재한다면
                user=User(line.split(',')[0],line.split(',')[1]) # 해당 줄에,로 분해 [0]이름[1]나이
                names.append(user) # 리스트에 저장
        f.close()
        return names
    except FileNotFoundError: # 예외처리 # 예외가 발생했을 때 실행되는 구역
        return [] # 빈배열 반환
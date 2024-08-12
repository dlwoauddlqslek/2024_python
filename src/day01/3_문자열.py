# 3_문자열
#[1] python 에서 문자열 사용방법
#(1) 큰따옴표
print("Hello World")
#(2) 작은따옴표
print('Hello World')
#(3) 큰다옴표 3개
print("""Hello World""")
#(4) 작은따옴표 3개
print('''Hello World''')

#[2] 문자열 안에 작은따옴표, 큰따옴표 포함할 때
print("Hello 'World'")      #""안에 ''
print('Hello "World"')      #''안에""
print('Hello \"World\"')    #이스케이프(제어)문자 , \', \"

#[3] 이스케이프 문자
print("Hello \nWorld\n")      #이스케이프(제어)문자, \n 줄바꿈
print("""Hello
World
""")                        #'''3개 """3개 이용한 문자열 줄바꿈
print('''Hello
World
''')
# 이스케이프 종류: \n 줄바꿈, \t 들여쓰기 \\ 백슬래시 출력, \' 작은따옴표 출력, \" 큰따옴표 출력

#[4] 문자열 연산하기
#(1) 문자열 더해서 연결하기 "문자열" + "문자열"
print("Python "+"is fun")
#(2) 문자열 곱하기, "문자열" * 반복수
print("Python"*2)
print("="*50)
print("My Program")
print("="*50)
#(3) 문자열 길이, len(문자열) : 해당 문자열의 길이 반환 함수
print(len("Python"))
#(4) 문자열 인덱싱, 문자열 내 문자 위치를 인덱스(번호) 표현
    # P[0] Y[1] T[2] H[[3] O[4] N[5]
    # 인덱스는 왼쪽은 0에서 시작, 오른쪽은 -1에서 시작
print("Python"[0]) # P, JAVA : "Python".chatAt(0)
print("Python"[2]) # t
print("Python"[4]) # o
#print("Python"[7]) # IndexError: string index out of range
print("Python"[-1]) # n, 뒤에서 부터
print("Python"[-3]) # h
print("Python"[-5]) # y
#(5) 문자열 슬라이싱, 인덱싱을 이용한 문자열 잘라내기
print("Python"[0:2])    # Py, 0인덱스 부터 2인덱스 전 까지. JAVA : "Python".subString
print("Python"[:3])     # Pyt, 생략시 0, 0~3 인덱스 전 까지
print("Python"[2:6])    # thon ,2~6 인덱스 전 까지
print("Python"[2:])     # thon, 생략시 마지막인덱스,2~6인덱스 전 까지
print("Python"[:])      # Python
print("Python"[2:-1])   # tho , t[2] ~ n[-1] 전 까지
print("Python"[-5:3])   # yt, y[-5] ~ h[3] 전 까지
#(활용)1
date="2024-08-12"
print(date[0:4])    #2024 , 2[0] 0[1] 2[2] 4[3], 0 ~ 4 전 까지
print(date[5:7])    #08 , 0[5] 8[6] , 5 ~ 7 전 까지
print(date[8:10])   #12 , 1[8] 2[9] , 8 ~ 10 전 까지

#[5] f 문자열 포매팅, python3.6버전 이상부터 사용 가능
    # f(접두사) 붙이고 ''문자열안에서 {} 이용한 연산이 가능하다.
    # {데이터:<자리수} : 왼쪽 정렬
    # {데이터:>자리수} : 오른쪽 정렬
    # {데이터:^자리수} : 가운데 정렬
    # {데이터:[공백문자][정렬기호][자리수]}
    # {데이터:[총자리수].[소수자리수]f}
print(f"나의 이름은 {'홍길동'}입니다. 나이는 {30}입니다.")
print(f"나의 이름은 {'홍길동'+'님'}입니다. 나이는 {30+1}입니다.")
print(f'{"python":<10}')    # 왼쪽 정렬, 10칸 차지
print(f'{"python":>10}')    # 오른쪽 정렬, 10칸 차지
print(f'{"python":^10}')    # 가운데 정렬, 10칸 차지
print(f'{"python":x<10}')   # 공백을 'x'로 채움
print(f'{"python":=^10}')   # 공백을 '='로 채움
print(f'{3.14159:0.1f}')    # 3.1, 소수점 첫째 자리 까지 표현
print(f'{3.14159:6.3f}')    # 3.142 소수점 셋째 자리 까지 표현
print(f'{'{python}'}')
print(f'{"python":!^12}')
# [1] 클래스의 멤버가 없는 구조
    # (1) 파이썬의 클래스 정의
class Member:
    pass
    # (2) 파이썬의 객체생성
m1 = Member()
# [2] 클래스의 생성자( __init__() 함수 )가 있는 구조
    # (1) 파이썬의 클래스 정의
class User:
    def __init__(self, name): # 생성자
        self.name = name # 속성/필드 정의
    # (2) 파이썬의 객체 생성 2개 생성
u1 = User("유재석")
u2 = User("강호동")

# [3] 클래스의 - ( __call__() 함수 )가 있는 구조
    # (1) 파이썬 클래스 정의
class Student:
    def __init__(self , name): # 생성자
        self.name = name
    def __call__(self,val):
        print(self.name ,val)
    # (2) 파이썬 객체 생성
s1= Student("유재석")
s2= Student("강호동")
# call 함수 호출해 보기 # 객체변수명() <--- call 함수를 호출한다는 뜻
s1(10) # 유재석 10
s2(20) # 강호동 20
Student("신동엽")(30) # call 함수는 함수명을 생략한다 # 객체 생성하고 바로 call 함수 호출시 # 신동엽 30
s1(s2) # 유재석 <__main__.Student object at 0x000002226BE24B00>
# !!!! 딥러닝의 신경망 모델에서 레이어(클래스)들 간의 서로 연결시 call 함수가 사용된다.
# 새로운레이어클래스명(레이어속성명=속성값,레이어속성명=속성값)(이전레이어객체변수명)
# Functional API 레이어 구조
# 1. 입력레이어변수명 = 입력레이어클래스명( 속성명=값 )
# 2. 새로운레이어변수명1 = 새로운레이어클래스명( 속성명=값 )( 입력레이어변수명 )

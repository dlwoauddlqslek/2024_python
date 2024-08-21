'''
    객체란? 논리적/물리적 정의한 실체물
    클래스란? 객체를 물리적으로 표현하기 위한 설계도
    인스턴스란? 클래스를 이용해서 객체를 물리적으로 만든 실체물


    - java
    class Calculator{
        int result; // 필드
        Calculator(){} // 생성자
        int add(int num){
            this.result+=num
            return this.result
        }
    }
    - java 객체
    Calculator cal1=new Calculator();
    Calculator cal2=new Calculator();
    - 객체가 메소드 호출
    cal1.add(3)
'''

#[1] 파이썬 클래스 만들기
class Calculator:
    def __init__(self): # 생성자
        self.result=0
    def add(self,num): # 메소드
        self.result+=num
        return self.result

#[2] 파이썬 객체 만들기
cal1=Calculator(); print(cal1) #<__main__.Calculator object at 0x0000025BE5941CA0>
cal2=Calculator(); print(cal2) #<__main__.Calculator object at 0x0000025BE5941CD0>

#[3] 파이썬 객체내 메소드 호출
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

#[4] 클래스의 생성자 정의
#(1) 과자 클래스 정의
class 과자틀:
    # 파이썬은 기본적으로 다중 생성자를 지원하지 않는다. 단일 생성자, __init__ 메소드는 1개
    # def __init__(self):
    #     self.과자재료1=None
    #     self.과자재료2 = None
    # 생성자1
    def __init__(self,재료1,재료2): #__init__ 생성자 역할을 하는 메소드
        # self: 해당 메소드를 실행하는 객체
        self.과자재료1=재료1 # self.필드명=매개변수 # 매개변수로 필드값 초기화하기
        self.과자재료2=재료2 # self.필드명=매개변수 # 매개변수로 필드값 초기화하기

#(2) 과자 객체 생성
var1=과자틀('밀가루','초코'); print(var1) #<__main__.과자틀 object at 0x0000026F870428A0>
var2=과자틀('밀가루','치즈'); print(var2) #<__main__.과자틀 object at 0x0000026F87042960>
#(3) 객체의 필드 호출
print(var1.과자재료1) # 첫번째 과자의 과자재료1 필드값 호출
print(var1.과자재료2) # 첫번째 과자의 과자재료2 필드값 호출
print(var2.과자재료1) # 두번째 과자의 과자재료1 필드값 호출
print(var2.과자재료2) # 두번째 과자의 과자재료2 필드값 호출
#(4) 객체의 필드 값 수정
#var3=과자틀(); print(var3) # 파이썬은 단일생성자만 가능
var2.과자재료2='녹차'
print(var2.과자재료2) #녹차









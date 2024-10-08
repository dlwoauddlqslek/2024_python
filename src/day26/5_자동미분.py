# p45
'''
    -함수(function)
        - 수학: 어떤 집합의 각 원소를 다른 어떤 집합의 유일한 원소에 대응시키는 이항 관계
        - 프로그래밍 함수: 어떠한 코드집합에 매개변수(N개)를 대입하고 결과변수(1개)를 받는 구조
'''

# 1. 텐서플로 모듈 호출
import tensorflow as tf
# 2. 선형 관계를 갖는 데이터 샘플 # y=3x-2
    # 1. 텐서플로의 랜덤 숫자 생성 객체 선언 # 시드값은 아무거나 # 시드란: 랜덤 생성할 때 사용되는 제어 정수값
g=tf.random.Generator.from_seed(2020) # 시드란: 랜덤 생성할 때 사용되는 제어 정수값
    # 2. 랜덤 숫자 생성 객체를 이용한 정규분포 난수를 10개 생성 해서 벡터(리스트) x에 저장한다.
    # .normal(shape=(축1, )) # .normal(shape=(축1,축2)) # .normal(shape=(축1,축2,축3))
x=g.normal(shape=(10,))
y=3*x -2
print(x.numpy()) # 독립 변수 # 피처
# [-0.20943771  1.2746525   1.213214   -0.17576952  1.876984    0.16379918
#   1.082245    0.6199966  -0.44402212  1.3048344 ]
print(y.numpy()) # 종속 변수 # 타겟
# [-2.628313    1.8239574   1.6396422  -2.5273085   3.630952   -1.5086024
#   1.2467351  -0.14001012 -3.3320663   1.9145031 ]

# 3. Loss 함수 정의 # 손실 함수(평균 제곱 오차)를 정의하는 함수
def cal_msg(x,y,a,b):
    y_pred=a*x+b # y값-종속(예측)= 계수(기울기)a*x(피처) + 상수항(y절편)
    squared_error=(y_pred - y)**2 # 예측 y와 실제 y간 차이의 제곱을 계산( 오차 제곱)
    mean_squared_error = tf.reduce_mean(squared_error) # 모든 오차 제곱의 평균을 계산하여 반환
    print(mean_squared_error)
    return mean_squared_error

# 4. 자동 미분 과정을 기록
a=tf.Variable(0.0) # 계수 # 텐서플로 변수에 0.0으로 초기화
b=tf.Variable(0.0) # y절편 # 텐서플로 변수에 0.0으로 초기화
  # a와 b를 미세하게 변경하면서 반복적으로 계산 하여 손실을 최소화 하는 값을 찾는다.
EPOCHS=200 # 훈련 횟수 # 에포크
for epoch in range(1,EPOCHS+1): #1~200 까지 (200회)
    # 200번을 반복하면서 목적: a와 b를 미세하게 변경하면서 차이가 가장 적은 값을 찾자.
    # 4-1 # tf.GradientTape() as 변수 : with 안에 잇는 계산식들을 모두 기록하는 역할 # mse를 tape에 기록한다.
    with tf.GradientTape() as tape:
        mse=cal_msg(x,y,a,b) # 위에서 정의한 손실함수를 계산한다.

    # 4-2 기울기 계산 # tape.gradient() 를 이용하여 mse에 대한 a와 b의 미분값(기울기)을 구한다.
    grad = tape.gradient(mse,{'a':a,'b':b}) # mse에 대한 a와 b를 딕셔너리 반환한다.
    d_a = grad['a']
    d_b= grad['b']

    # 4-3 # .assign_sub() 텐서플로 변수에 매개변수를 원본값에서 뺀 값으로 변수값을 수정하는 함수
    a.assign_sub(d_a*0.05)   # 현재값의 5% 감소
    b.assign_sub(d_b * 0.05) # 0.05 감소

    # 4-4 중간 계산 확인
    if epoch %20==0: # 20번 마다 # epoch=반복횟수 # mse: 평균제곱오차 # a 계수 # b 상수항
        print(f'{epoch},{mse:.4f},{a.numpy():.4f},{b.numpy():.4f}') # mse에 대한 a와 bfmf 딕셔너리 반환한다.

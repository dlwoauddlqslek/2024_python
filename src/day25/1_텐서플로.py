# 텐서플로: 텐서(다차원데이터)를 플로(흐름)에 따라 연산하는 과정을 제공하는 라이브러리

# [1] 모듈 호출
import tensorflow as tf
# [2] 텐서플로2에서 즉시 실행 모드인지 확인하는 함수
print(tf)
print(tf.executing_eagerly()) # True
# [3] 텐서플로 연산
a=1
b=2
c=tf.math.add(a,b)
print(c) # tf.Tensor(3, shape=(), dtype=int32)
print(type(c)) # <class 'tensorflow.python.framework.ops.EagerTensor'>
print(tf.math.add) # 수학 관련 모듈 tf.math
# [4] 텐서 객체에서 결과값을 추출 # .numpy()
print(c.numpy()) # 텐서 객체에서 결과값을 추출 # 3
# [5] 텐서( 상수: 스칼라) # tf.Tensor(값, shape=(배열크기), 타입=)
    # 1. 스칼라 정의
a=tf.constant(1)
b=tf.constant(2)
print(a)    # tf.Tensor(1, shape=(), dtype=int32)
print(b)    # tf.Tensor(2, shape=(), dtype=int32)
    # 2. 랭크 확인 # .rank()
print(tf.rank(a)) # tf.Tensor(0, shape=(), dtype=int32)
    # 3. 스칼라 데이터 타입변환 # .cast(스칼라객체, tf.타입)
a = tf.cast( a, tf.float32) # a스칼라객체의 값을 실수로 변환
b = tf.cast( b, tf.float32)
print(a) # tf.Tensor(1.0, shape=(), dtype=float32)
print(b) # tf.Tensor(2.0, shape=(), dtype=float32)
    # 4. 수학적 함수 # .math
        # (1) .math.add(값1, 값2) : 덧셈
c= tf.math.add(a,b)
print(c) # tf.Tensor(3.0, shape=(), dtype=float32)
print(tf.rank(c)) # tf.Tensor(0, shape=(), dtype=int32)
        # (2) .math.subtract(값1,값2): 뺄셈
print(tf.math.subtract(a,b))
print(tf.math.multiply(a,b)) # 곱셈
print(tf.math.divide(a,b))   # 나눗셈
print(tf.math.mod(a,b))      # 나머지
print(tf.math.floordiv(a,b)) # 몫
print(a+b) # tf.Tensor(3.0, shape=(), dtype=float32)
print(a-b)
print(a*b)
print(a/b)
print(a%b) # 나머지
print(a//b) # 몫
# [6] 텐서(1차원 리스트: 벡터) # tf.Tensor(, shape=(원소개수,), dtype=)
import numpy as np # 넘파일 모듈 호출
vec1 = tf.constant([10,20,30],dtype=tf.float32) # 파이썬 리스트
vec2 = tf.constant(np.array([10,10,10]),dtype=tf.float32) # 넘파일 배열
print(vec1) # tf.Tensor([10 20 30], shape=(3,), dtype=int32)
print(vec2) # tf.Tensor([10 10 10], shape=(3,), dtype=int32)
# 랭크 확인
print(tf.rank(vec1)) # tf.Tensor(1, shape=(), dtype=int32)
print(tf.rank(vec2)) # tf.Tensor(1, shape=(), dtype=int32)
# 벡터 연산
print(vec1+vec2) # tf.Tensor([20 40 60], shape=(3,), dtype=int32)
print([10,20,30]+[10,20,30]) # [10, 20, 30, 10, 20, 30]
print(vec1-vec2)
print(vec1*vec2)
print(vec1/vec2)
print(vec1%vec2)  #
print(vec1//vec2) #
print(vec1 **2)   # 거듭제곱 # .math.square()
print(vec1 **0.5) # 제곱근   # .math.sqrt()
# 벡터내 요소 총합계
print(tf.reduce_sum(vec1)) # tf.Tensor(60, shape=(), dtype=int32)
print(vec1+1) # 브로드캐스팅 # tf.Tensor([11. 21. 31.], shape=(3,), dtype=float32)

# [6] 텐서객체(2차원 리스트: 행렬) # tf.Tensor([[10 20][30 40]], shape=(행개수=벡터개수, 열개수=벡터내 원소개수), dtype=int32)
mat1=tf.constant([[10,20],[30,40]]) # 전체를 감싼 대괄호 내 원소개수: 행개수/벡터개수 # 내부 대괄호내 원소개수: 열개수/스칼라개수
print(mat1) # 행과 열이라는 축이 2개라서 랭크/차수: 2
'''
tf.Tensor(
[[10 20]
 [30 40]], shape=(2, 2), dtype=int32)
'''
# 랭크 확인
print(tf.rank(mat1)) # .Tensor(2, shape=(), dtype=int32) # 2
# mat2= tf.stack(벡터, 벡터)
mat2=tf.stack([[1,1],[-1,2]]) # 1차원 리스트 2개를 2차원으로 변환
print(mat2)
'''
tf.Tensor(
[[ 1  1]
 [-1  2]], shape=(2, 2), dtype=int32)
'''
print(tf.rank(mat2)) # tf.Tensor(2, shape=(), dtype=int32)
# 행렬 연산
print(tf.math.multiply(mat1,mat2))
print(mat1*mat2)
print(mat1+mat2)    # .math.add(mat1,mat2)
print(mat1-mat2)    # .math.subtract(mat1,mat2)
print(mat1/mat2)    # .math.divide(mat1,mat2)
print(mat1%mat2) # 오류 # division by zero 조심
print(tf.math.mod(mat1,mat2))
print(mat1//mat2)
print(tf.math.multiply(mat1,3)) # 브로드캐스팅
# 행(가로)열(세로)곱(곱셈) 연산
print(tf.matmul(mat1,mat2))
'''
[[-10  50]
 [-10 110]], shape=(2, 2), dtype=int32)
'''
'''
    인공지능(AI)
        빅데이터: 많은 자료             
        머신러닝: 자료들의 학습 모델     (사이킷런 라이브러리)
        딥러닝: 복잡한 자료들의 학습 모델 (텐서플로 라이브러리)

    텐서플로 자료구조
    
    스칼라     벡터          매트릭                   텐서
    rank-0    rank-1       rank-2                  rank-3
    값        리스트        2차원리스트               3차원리스트
    차수-0    차수(축)-1     차수(축)-2               차수(축)-3
    x         한방향:x      두방향:가로(x)세로(y)     세방향: 가로(x)세로(y)높이(z)
'''

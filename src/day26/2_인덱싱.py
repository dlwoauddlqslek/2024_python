# p36
import tensorflow as tf
'''
- 인덱싱
    - 원소가 저장된 순서 번호
- 슬라이싱
    -[시작:끝(미만)]
'''
# 1. 벡터
vec=tf.constant([10,20,30,40,50])
print(vec)
print(vec[0]) # tf.Tensor(10, shape=(), dtype=int32)
print(vec[0].numpy()) # 10
print(vec[-1]) # tf.Tensor(50, shape=(), dtype=int32)
print(vec[0:3]) # 0~2 # 벡터 # tf.Tensor([10 20 30], shape=(3,), dtype=int32)
# 2. 행렬
mat=tf.constant([[10,20,30],[40,50,60]])
print(mat[0,2]) # [행인덱스, 열인덱스] # 첫번째 행, 세번째 열 # tf.Tensor(30, shape=(), dtype=int32)
print(mat[0,:]) # [행(슬라이싱), 열(슬라이싱)] # 첫번째 행, 전체 열 [:] # 벡터 # tf.Tensor([10 20 30], shape=(3,), dtype=int32)
print(mat[:,1]) # 전체 행[:], 두번째 열 # 벡터 # tf.Tensor([20 50], shape=(2,), dtype=int32)
print(mat[:,:]) # 전체 행, 전체 열 # tf.Tensor([[10 20 30] [40 50 60]], shape=(2, 3), dtype=int32)
# 3. 3차원 텐서
tensor= tf.constant( # (행렬2개, 벡터2개, 스칼라3개) # (높이=2, 행=2개 ,열=3개)
    [ # 축1 - 고차원텐서(3차원리스트)
        [ # 축2 - 행렬(2차원리스트)
            [10,20,30],[40,50,60] # 축3 - 벡터(1차원리스트)
        ],
        [
            [-10,-20,-30],[-40,-50,-60]
        ]
    ]
)
print(tensor)
print(tensor[0,:,:]) # 축1에서 첫번째 인덱스, 축2에서 전체인덱스, 축3에서 전체인덱스 # 행렬 # (2,3) # [[10 20 30][40 50 60]], shape=(2, 3), dtype=int32)
print(tensor[:,:2,:2])
'''
tf.Tensor(
[[[ 10  20]
  [ 40  50]]

 [[-10 -20]
  [-40 -50]]], shape=(2, 2, 2), dtype=int32)
'''

# 연습
# 1. 벡터
vector=tf.constant([10,20,30,40,50])
# 첫번째 스칼라 출력
print(vector[0])
# 뒤에서 두번째 스칼라 출력
print(vector[-2])
# 앞에서 3개 요소 슬라이싱
print(vector[:3])
# 뒤에서 4개 요소 슬라이싱
print(vector[-4:])
# 2. 행렬
matrix=tf.constant([[1,2,3],[4,5,6],[7,8,9]])
# 첫번째 행, 두번재 열 요소 인덱싱
print(matrix[0,1])
# 세번째 행, 첫번째 열 요소 인덱싱
print(matrix[2,0])
# 첫번째 행 전체 슬라이싱
print(matrix[0,:])
# 두번째 열 전체 슬라이싱
print(matrix[:,1])
# 3. 3차원텐서
tensor=tf.constant([[[1,2],[3,4]],[[5,6],[7,8]]])
# 가장 첫뻔째 요소 인덱싱
print(tensor[0,0,0])
# 가장 마지막 요소 인덱싱
print(tensor[-1,-1,-1])
# 첫번째 행렬 슬라이싱
print(tensor[0,:,:])
# 두번째 행렬의 첫번째 행 슬라이싱
print(tensor[1,0,:])
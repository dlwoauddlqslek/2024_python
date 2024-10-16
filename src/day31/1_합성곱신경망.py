# 1. 데이터셋 준비
'''
- 딥러닝 프로세스(절차)
    1. 데이터 수집
    2. 데이터 전처리 : 수집된 데이터를 신경망 모델에 적합하게 수정
    3. 데이터 분할 : 훈련용 데이터와 검증/데이터용으로 나눈다. 주로 7:3 vs 8:2
    4. 모델 설계(구축)
        1. Sequential API(이미 만들어진 클래스) ,Functional API(이미 만들어진 클래스)
        2. 레이어 구성 : 입력 레이어 ---> 은닉 레이어(conv2D,MaxPooling2D,Flatten)등등 ---> 은닉 레이어 ---> 출력 레이어 순으로 구성
        3. 활성화 함수 : 각 레이어에서 학습된 값을 비선형으로 변환할 때 사용. 주로 Relu, softmax 함수 사용
    5. 모델 컴파일 : 모델ㅇ들 어떻게 학습하고 평가하는지 설정
        1. 옵티마이저 : 모델의 가중치를 업데이트하는 방법의 알고리즘/계산법, adam: 학습률 기반으로 최적화 알고리즘, sgd: 확률적 경사 하강법
        2. 손실함수 : 실제값과 예측과의 차이, 분류모델 : sparse_categorical_crossentropy, 회귀: mean_squared_error
        3. 평가지도 : 모델의 성능을 평가하는 지표, 분류모델 : accuracy, 회귀 : mse
    6. 모델 학습
        1. 에포크 : 전체 훈련 데이터를 한 번 사용되는 것을 1 에포크, 10 에포크 이면 전체 훈련을 10번
        2. 검증 : validation_data 학습 중에 검증/테스트 데이터를 사용하여 모델의 손실,평가를 확인할 수 있다.
    7. 모델 평가 ---> 모델 튜닝(하이퍼 파라미터)
        1. evaluation() : 최종 성능의 손실함수와 평가지표 결과를 볼 수 있다.
---> 모델 튜닝(하이퍼 파라미터)
        - 학습률, 배치 크기, 레이어 수, 뉴런(노드) 수, 활성화 함수, 에포크 등등 여러 하이퍼 파라미터 조정하기
    8. 모델 예측
        1. .predict()
'''
import tensorflow as tf
import numpy as np

# mnist 손글씨 이미지 데이터 로드
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_valid,y_valid) = mnist.load_data()

print(x_train.shape,y_train.shape)
print(x_valid.shape,y_valid.shape)

# 새로운 출력 값 배열 생성(홀수 : 1, 짝수: 0)
y_train_odd=[]
for y in y_train:
    if y%2==0:
        y_train_odd.append(0)
    else:
        y_train_odd.append(1)
y_train_odd=np.array(y_train_odd) # 넘파이 배열
y_train_odd.shape

print(y_train[:10])
print(y_train_odd[:10])

y_valid_odd=[]
for y in y_valid:
    if y%2==0:
        y_valid_odd.append(0)
    else:
        y_valid_odd.append(1)
y_valid_odd=np.array(y_valid_odd) # 넘파이 배열

# 3. 정규화
x_train = x_train/255.0
x_valid = x_valid/255.0

# 4. 채널 추가 # 마지막 인덱스(-1)의 새로운 축 추가
x_train_in = tf.expand_dims(x_train,-1)
x_valid_in = tf.expand_dims(x_valid,-1)
print(x_train_in.shape, x_train_in.shape) #

# Functional API를 사용하여 모델 생성
inputs = tf.keras.layers.Input(shape=(28,28,1))

conv = tf.keras.layers.Conv2D(32,(3,3), activation='relu')(inputs)
pool = tf.keras.layers.MaxPooling2D(2,2)(conv)
flat = tf.keras.layers.Flatten()(pool)

flat_inputs = tf.keras.layers.Flatten()(inputs)
concat = tf.keras.layers.Concatenate()([flat,flat_inputs])
outputs = tf.keras.layers.Dense(10, activation='softmax')(concat)

model = tf.keras.models.Model(inputs=inputs,outputs=outputs)

model.summary()

# 모델 컴파일
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

# 모델 훈련
history=model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=1)

# 모델 성능
val_loss,val_acc=model.evaluate(x_valid_in,y_valid)
print(val_loss,val_acc)

# 다중 출력 분류 모델 ( 1. 다중분류[0~9] 2. 이진분류[0,1] )
inputs = tf.keras.layers.Input(shape=(28,28,1), name='inputs')

conv = tf.keras.layers.Conv2D(32,(3,3), activation='relu', name='conv2d_layer')(inputs)
pool = tf.keras.layers.MaxPooling2D((2,2), name='maxpool_layer')(conv)
flat = tf.keras.layers.Flatten(name='flatten_layer')(pool)

flat_inputs = tf.keras.layers.Flatten()(inputs)
concat = tf.keras.layers.Concatenate()([flat,flat_inputs])
digit_outputs = tf.keras.layers.Dense(10,activation='softmax', name='digit_dense')(concat)

odd_outputs = tf.keras.layers.Dense(1, activation='sigmoid', name='odd_dense')(flat_inputs)

model = tf.keras.models.Model(inputs=inputs, outputs=[digit_outputs,odd_outputs])

model.summary()
print(model.input)
print(model.output)

# 모델 컴파일
model.compile(optimizer='adam',loss={'digit_dense':'sparse_categorical_crossentropy','odd_dense':'binary_crossentropy'},
              loss_weights={'digit_dense':1,'odd_dense':0.5},
              metrics={'digit_dense':'accuracy','odd_dense':'accuracy'})

# 모델 훈련
history = model.fit({'inputs':x_train_in},{'digit_dense':y_train,'odd_dense':y_train_odd},
                    validation_data=({'inputs':x_valid_in},{'digit_dense':y_valid,'odd_dense':y_valid_odd}),epochs=1)

# 모델 성능
model.evaluate({'inputs':x_valid_in},{'digit_dense':y_valid,'odd_dense':y_valid_odd})

# 샘플 이미지 출력
import matplotlib.pylab as plt

def plot_image(data,idx):
    plt.figure(figsize=(5,5))
    plt.imshow(data[idx])
    plt.axis("off")
    plt.show()
plot_image(x_valid,0)

# 모델 예측
print(y_valid[0]) # 정답 : 7
digit_preds,odd_preds = model.predict(x_valid_in) # 예측
print(digit_preds[0])
print(odd_preds[0])

# 전이학습
# 앞의 모델에서 flatten_layer 출력을 추출
# (1) 기존의 Functional API 로 생성한 모델에서 특정 레이어 추출해서 새로운 functional API 모델 생성하기.
base_model_output = model.get_layer('flatten_layer').output # 특정 레이어와 연결된 레이어까지 추출 - conv<-pooling<-flatten
base_model = tf.keras.models.Model(inputs=model.input, outputs=base_model_output, name='base')
print(base_model.summary()) # 기존모델에서 입력층과 출력층은 플래튼까지 레이어
# (2) 출력레이어 추가 하는 새로운 Sequential API로 모델 생성하기
digit_model = tf.keras.Sequential([base_model , tf.keras.layers.Dense(10,activation='softmax'),])
print(digit_model.summary())
# functional API( input -> conv -> pooling -> flatten ) -> Dense
# (3) 모델 컴파일
digit_model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# (4) 모델 훈련
digit_model.fit(x_train_in,y_train, validation_data=(x_valid_in,y_valid), epochs=3)

# (5)
base_model_frozen = tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base_frozen')
base_model_frozen.trainable = False # 모델의 파라미터 값이 고정되면서 훈련을 통해서 업데이트 되지 않는다. 훈련이 안된다.
print(base_model_frozen.summary())
# 1. Functional Api 적용
dense_output = tf.keras.layers.Dense(10, activation='softmax')(base_model_frozen.output)
digit_model_frozen=tf.keras.models.Model(inputs=base_model_frozen.input,outputs=dense_output)
print(digit_model_frozen.summary())

digit_model_frozen.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

digit_model_frozen.fit(x_train_in,y_train,
                       validation_data=(x_valid_in,y_valid),
                       epochs=3)

# 2. Sequential API 적용
base_model_frozen2 = tf.keras.models.Model(inputs=model.input,outputs=base_model_output,name='base_frozen2')
base_model_frozen2.get_layer('conv2d_layer').trainable=False
print(base_model_frozen2.summary())

dense_output2 = tf.keras.layers.Dense(10, activation='softmax')(base_model_frozen2.output)
digit_model_frozen2=tf.keras.models.Model(inputs=base_model_frozen2.input,outputs=dense_output2)
print(digit_model_frozen2.summary())

digit_model_frozen2.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])

digit_model_frozen2.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=3)
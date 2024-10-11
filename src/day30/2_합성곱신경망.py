import tensorflow as tf
import matplotlib.pyplot as plt
# 데이터셋 # 10가지 종류의 이미지 데이터셋[비행기0,자동차1,새2,고양이3,사슴4,개5,개구리6,말7,배8,트럭9]
cifar10=tf.keras.datasets.cifar10
# 칼라 이미지의 합성곱 모델 만들기

(x_train,y_train),(x_valid,y_valid) = cifar10.load_data()
print(x_train.shape) # (50000, 32, 32, 3)




x_train=x_train/255.0
x_valid=x_valid/255.0

model=tf.keras.Sequential([
    tf.keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,3)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64,(3,3),activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64,activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history=model.fit(x_train,y_train,
                  validation_data=(x_valid,y_valid),
                  epochs=10
                  )

########### 예측
# 1. 파이썬 OpenCV : 이미지파일을 파이썬으로 호출 하는 모듈 제공 한다.
import cv2 # opencv-python 설치
# 2. 외부 이미지 가져오기
img = cv2.imread('cat2.jpg')
print(img)
print(img.shape) # (336, 575, 3): 원본이미지는 가로 336픽셀 세로 575픽셀 컬러(3채널)
# 3. 이미지의 사이즈 변경
img = cv2.resize(img, dsize=(32,32)) # 모델이 학습한 사이즈와 동일하게 변경 # (32,32,3) 픽셀 줄이기
img=img/255.0
# 4. 변경된 이미지 시각화
# cv2.imshow('img',img)
# cv2.waitKey()
# 5. 모델을 이용한 새로운 이미지 예측하기
result = model.predict(img[tf.newaxis,...]) # (32,32,3) --> (1,32,32,3)
print(tf.argmax(result[0]).numpy()) # 가장 높은 확률을 가진 종속변수

img = cv2.imread('cat3.jpg')
print(img)
print(img.shape) # (336, 575, 3): 원본이미지는 가로 336픽셀 세로 575픽셀 컬러(3채널)
# 3. 이미지의 사이즈 변경
img = cv2.resize(img, dsize=(32,32)) # 모델이 학습한 사이즈와 동일하게 변경 # (32,32,3) 픽셀 줄이기
img=img/255.0
# 4. 변경된 이미지 시각화
# cv2.imshow('img',img)
# cv2.waitKey()
# 5. 모델을 이용한 새로운 이미지 예측하기
result = model.predict(img[tf.newaxis,...]) # (32,32,3) --> (1,32,32,3)
print(tf.argmax(result[0]).numpy()) # 가장 높은 확률을 가진 종속변수
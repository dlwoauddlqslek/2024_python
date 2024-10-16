import tensorflow as tf
# 1. 데이터셋 로드, 10가지 종류의 의류 이미지 데이터셋
'''
                    "T-shirt/top",
                    "Trouser",
                   "Pullover",
                    "Dress",
                    "Coat",
                    "Sandal",
                    "Shirt",
                    "Sneaker",
                    "Bag",
                    "Ankle boot",
'''
fashion_mnist=tf.keras.datasets.fashion_mnist
(x_train,y_train),(x_valid,y_valid)=fashion_mnist.load_data()
# Functional API 이용한 모델 생성(다중 입력)과 예측 테스트
print(x_train.shape,y_train.shape)
print(x_valid.shape,y_valid.shape)

x_train=x_train/255.0
x_valid=x_valid/255.0

x_train_in = tf.expand_dims(x_train,-1)
x_valid_in = tf.expand_dims(x_valid,-1)

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
history=model.fit(x_train_in,y_train,validation_data=(x_valid_in,y_valid),epochs=10)

# 모델 성능
val_loss,val_acc=model.evaluate(x_valid_in,y_valid)
print(val_loss,val_acc)
import matplotlib.pylab as plt
def plot_image(data,idx):
    plt.figure(figsize=(5,5))
    plt.imshow(data[idx])
    plt.axis("off")
    plt.show()
plot_image(x_valid,0)
print(y_valid[0])

import cv2

img = cv2.imread('boots.jpg')
img=cv2.resize(img,dsize=(28,28))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=img/255.0
img = img[..., tf.newaxis]
result=model.predict(img[tf.newaxis,...])
print(tf.argmax(result[0]).numpy())
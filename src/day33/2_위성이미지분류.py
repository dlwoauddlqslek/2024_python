# day32 --> 1.위성이미지분류.py
# 딥러닝 프로세스
# (1) 데이터 수집
# (2) 데이터 전처리 / 데이터 분할
# (3) 모델 설계(구축)
# (4) 모델 컴파일
# (5) 모델 학습 ----> 모델 튜닝(최적의 하이퍼 파라미터 찾기) -> (3)
# (6) 모델 평가 및 예측

# (1) 데이터 수집
import tensorflow as tf
import numpy as np
import json
import matplotlib.pyplot as plt
import tensorflow_datasets as tfds
import chardet
from tensorflow.keras.applications import ResNet50V2
(train_ds , valid_ds) , info  = tfds.load( 'eurosat/rgb' , # 다운로드 할 데이터셋 이름
           split=['train[:80%]' , 'train[80%:]'] , # 80%의 데이터를 훈련용 , 20%를 검증용으로 분할하기.
           shuffle_files=True , # 파일을 무작위로 섞어 데이터를 로드한다.
           as_supervised=True , # 이미지와 레이블로 구성된 튜플로 가져오기.
           with_info = True ,  # 데이터셋의 메타정보(데이터셋설명) 가져오기.
           data_dir = 'c:/dataset/' # 현재 py 파일이 위치한 폴더내 하위 폴더로 'dataset' 폴더안에 '데이터셋' 를 다운로드 하겠다.
           )
print( train_ds )
print( valid_ds )
print( info )
# .show_examples() : 샘플의 이미지와 분류 레이블 출력해주는 함수
tfds.show_examples( train_ds , info)
# .as_dataframe()
print( tfds.as_dataframe( valid_ds.take(10) , info ) )
# 전체 레이블 수 확인
NUM_CLASSES = info.features['label'].num_classes
# 특정 번호의 레이블 확인
print( info.features['label'].int2str(6) ) # PermanentCrop : 영구작물
# 0:경작지 1.숲 2.식물 3.고속도로 4.산업지역 5.목초지  6:영구작물 7.주거지역 8.강 9:바다/호수

# (2) 데이터 전처리
BATCH_SIZE = 64 # 배치란? 한번에 처리하는 데이터의 묶음 단위 의미한다.
    # 데이터를 배치로 나눠서 처리하면 메모리 사용을 최적할수 있다.
    # 모델이 전체를 한번에 처리하지 않고 데이터를 묶음(배치) 단위로 나누어 처리한다. - 배치 처리
BUFFER_SIZE = 1000 # 버퍼란? 임시 저장공간
    # 셔플 할때 버퍼에 데이터를 1000를 가져와서 임시로 저장하는 공간이다.
    # 셔플 : 일반적으로 정형화된 데이터들을 순서대로 넣으면 모델의 특정 패턴이 치우치게 될수 있기 때문에 섞어준다.

def preprocess_data( image , label ) :
    image = tf.cast( image , tf.float32 ) / 255.0 # 이미지타입을 float32 변환하고 # 0~255 -> 0~1 정규화
    return  ( image , label ) # 이미지와 레이블을 튜플구조로 반환하기
# JS map 함수
# newArray = [ 3 , 2 , 1 ].map( ( value )->{ return value + 10  } )
# newArray( 13 , 12 , 11 )

# num_parallel_calls = tf.data.AUTOTUNE : 병렬처리(병렬 매핑)
train_data = train_ds.map(preprocess_data , num_parallel_calls = tf.data.AUTOTUNE )
valid_data = valid_ds.map(preprocess_data , num_parallel_calls = tf.data.AUTOTUNE )

# 훈련용데이터를 셔플링(가중치-업데이트o) 하고 캐시(기록) 제외한  오토튠을 적용했다.
# 검증용데이터를 셔플링(가중치-업데이트x) 하지 않고 캐시(기록) 하고  오토튠을 적용했다.
train_data = train_data.shuffle( BUFFER_SIZE ).batch( BATCH_SIZE ).prefetch( tf.data.AUTOTUNE )
valid_data = valid_data.batch( BATCH_SIZE ).cache().prefetch( tf.data.AUTOTUNE )
# cache() : 캐시( 기록 )란 검증데이터셋 메모리를 캐시한다.
# 한번 호출한 검증데이터는 메모리에 기록하여 다음에 호출시 빠르게 접근할수 있도록 하는 함수

# prefetch( tf.data.AUTOTUNE ) : 데이터 전처리 와 훈련을 병렬로 수행하여 학습 속도를 향상 할수 있다.

# 모델링 함수
def build_model():
    model = tf.keras.Sequential([ # Sequential API 이용한 모델 구축
        # ======================== [ Convolution 층 = 합성곱 = 연산층 = 특징 찾기 ]
        # 1. 합성곱(신경망) 레이어
        tf.keras.layers.BatchNormalization(),
        # 배치 : 모델링에 있어서 병렬처리에 배치(묶음) 단위로 처리하면 더 빠르고 안정적으로 학습할 수 있다. # 과대적합을 줄이기 가능하다.
        # BatchNormalization 레이어가 없어도 모델 구현이 가능하지만 모델의 최적화에 필요한 레이어 # 주로 AUTOTUNE 사용시 사용된다.
        tf.keras.layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # 1. 합성곱(신경망) 레이어 # 복잡한 신경망 구현하기 위해 2번의 합성곱을 실행했다.
        # 1번만 합성곱 연산으로 모델 구축 가능하지만 더 많은 특징을 찾기 위해 2번의 레이어 만들었다.
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # ======================== [ Classifier 층 = 출력층 = 예측분류층 = 특징 학습 ]
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'), # Dense : 완전 연결된 신경망 층, 이전 node(뉴런) 받아서 패턴 학습 한다.
        # 주로 노드 개수는 32 64 128 사용한다.
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation='softmax'),
    ])
    return model
model = build_model()
# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 모델 훈련
history = model.fit(train_data,
                    validation_data=valid_data,
                    epochs=3)

# 손실 함수, 정확도 그래프 그리기 # 교제에서 제외된 부분
def plot_loss_acc(history,epoch):
    loss = history.history['loss']
    val_loss=history.history['val_loss']
    acc=history.history['accuracy']
    val_acc=history.history['val_accuracy']

    fig,axes=plt.subplots(1,2)
    axes[0].plot(range(1,epoch+1),loss)
    axes[0].plot(range(1, epoch + 1), val_loss)

    axes[1].plot(range(1, epoch + 1), acc)
    axes[1].plot(range(1, epoch + 1), val_acc)

    plt.show()

plot_loss_acc(history, 3)
# 샘플 이미지
image_batch, label_batch = next(iter(train_data.take(1)))
image = image_batch[0]
label = label_batch[0].numpy()
plt.imshow(image)
plt.title(info.features["label"].int2str(label))
# 데이터 증강 전후를 비교하는 시각화 함수를 정의
def plot_augmentation(original, augmented):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[1].imshow(augmented)
    axes[1].set_title("Augmented")
    plt.show()
# 좌우 뒤집기
lr_flip = tf.image.flip_left_right(image)
plot_augmentation(image, lr_flip)
# 상하 뒤집기
ud_flip = tf.image.flip_up_down(image)
plot_augmentation(image, ud_flip)
# 회전 (90도)
rotate90 = tf.image.rot90(image)
plot_augmentation(image, rotate90)
# transpose (행렬의 도치, 행과 열의 위치를 바꿈)
transpose = tf.image.transpose(image)
plot_augmentation(image, transpose)
# 이미지 자르기 1
crop1 = tf.image.central_crop(image, central_fraction=0.6)
plot_augmentation(image, crop1)
# 이미지 자르기 2
img = tf.image.resize_with_crop_or_pad(image, 64 + 20, 64 + 20)  # 사이즈 키우기
crop2 = tf.image.random_crop(img, size=[64, 64, 3])
plot_augmentation(image, crop2)
# 이미지 밝기
brightness = tf.image.adjust_brightness(image, delta=0.3)
plot_augmentation(image, brightness)
# 이미지 채도
saturation = tf.image.adjust_saturation(image, saturation_factor=0.5)
plot_augmentation(image, saturation)
# 이미지 대비
contrast = tf.image.adjust_contrast(image, contrast_factor=2)
plot_augmentation(image, contrast)
# 이미지 증강 전처리
def data_augmentation(image, label):
    image = tf.image.random_flip_left_right(image)  # 좌우 반전
    image = tf.image.random_flip_up_down(image)  # 상하 반전
    image = tf.image.random_brightness(image, max_delta=0.3)  # 밝기 변화
    image = tf.image.random_crop(image, size=[64, 64, 3])  # 크기 자르기
    image = tf.cast(image, tf.float32) / 255  # 0 ~ 1 정규화
    return image, label  # 튜플 구조로 return
train_aug = train_ds.map(data_augmentation, num_parallel_calls=tf.data.AUTOTUNE)
valid_aug = valid_ds.map(data_augmentation, num_parallel_calls=tf.data.AUTOTUNE)
train_aug = train_aug.shuffle(BUFFER_SIZE).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)
valid_aug = valid_aug.batch(BATCH_SIZE).cache().prefetch(tf.data.AUTOTUNE)
# print(train_aug)
# <_PrefetchDataset element_spec=(TensorSpec(shape=(None, 64, 64, 3), dtype=tf.float32, name=None), TensorSpec(shape=(None,), dtype=tf.int64, name=None))>
# print(valid_aug)
# <_PrefetchDataset element_spec=(TensorSpec(shape=(None, 64, 64, 3), dtype=tf.float32, name=None), TensorSpec(shape=(None,), dtype=tf.int64, name=None))>
# 모델 생성
aug_model = build_model()
# 모델 컴파일
aug_model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# 모델 훈련
aug_history = aug_model.fit(train_aug, validation_data=valid_aug, epochs=3)
# 손실 함수, 정학도 그래프 그리기
# plot_loss_acc(aug_history, 50)
pre_trained_base = ResNet50V2(include_top= False, weights= "imagenet", input_shape=[64, 64, 3])
pre_trained_base.trainable = False
def build_trainsfer_classifier():
    model = tf.keras.Sequential([
        # pre_trained Base
        pre_trained_base,
        # Classifier 출력층
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(NUM_CLASSES, activation="softmax")
    ])
    return model
tc_model = build_trainsfer_classifier()
tc_model.summary()
tc_model.compile(optimizer="adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
tc_history = tc_model.fit(train_aug, validation_data=valid_aug, epochs= 3)

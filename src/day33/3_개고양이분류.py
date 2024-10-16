# 실무에서는 데이터셋을 웹에서 로드하는 경우가 거의 없다
# 직접 이미지를 로드하는 경우가 더 많다.
# 강의 카톡방에 cat-and-dog.zip 다운로드 받아 현재 day33에 넣기
import zipfile
import os
import tensorflow as tf
# 1. 데이터 준비( 교재와 다르게 구글드라이브가 아닌 로컬pc에서 준비 )
    # 데이터 경로 위치
source_filename = 'cat-and-dog.zip' #(1) zip파일이 위치한 파일명
extract_folder = 'c:/dataset'       #(2) zip파일을 압축해제할 폴더명
    # (파이썬 코드로) 압축 해제
with zipfile.ZipFile(source_filename,'r') as zipObj:
    zipObj.extractall(extract_folder) # 지정한 경로에 압축해제 하기
        # zipfile.ZipFile(source_filename,'r') : zip파일을 읽기모드로 읽어와서 zipObj 변수에 담기
        # 파일객체변수명.extractall(압축해제할폴더경로)
    # 훈련용, 검증용 저장위치 지정 # C:\dataset\archive
train_dir = os.path.join(extract_folder,"archive/training_set/training_set")
valid_dir = os.path.join(extract_folder,"archive/test_set/test_set")
print(train_dir)
print(valid_dir)

# 2. 정규화
from tensorflow.keras.preprocessing.image import ImageDataGenerator # 모듈 호출
image_gen = ImageDataGenerator(rescale=(1/255.0)) # 이미지 데이터를 0부터 255-> 0부터 1 정규화 진행

# 3. 이미지 제네레이터 : 한번에 많은 데이터를 가져오면 메모리에 문제가 발생하므로 이미지를 배치(묶음)단위로 반복해서 가져오기
train_gen = image_gen.flow_from_directory(train_dir, # 훈련용 데이터 저장된 위치
                                          batch_size=16, # 배치 단위
                                          target_size=(244,244), # 이미지 사이즈 변경
                                          classes=['cats','dogs'], # 문자로된 클래스(종속)를 cats->0, dogs->1
                                          class_mode='binary', # 이진 분류
                                          seed=2020 # 난수 시드값
                                          )
valid_gen = image_gen.flow_from_directory(valid_dir, # 훈련용 데이터 저장된 위치
                                          batch_size=16, # 배치 단위
                                          target_size=(244,244), # 이미지 사이즈 변경
                                          classes=['cats','dogs'], # 문자로된 클래스(종속)를 cats->0, dogs->1
                                          class_mode='binary',
                                          seed=2020
                                          )
#
class_labels=['cats','dogs']
batch=next(train_gen)
images = batch[0] # 독립변수 # 개 또는 고양이 이미지
labels = batch[1] # 종속변수 # 이미지 정답

import matplotlib.pyplot as plt
for i in range(16):
    ax=plt.subplot(4,8,i+1)
    plt.imshow(images[i])
    plt.title(class_labels[int(labels[i])]) # int로 변환
plt.show()

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
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        # ======================== [ Classifier 층 = 출력층 = 예측분류층 = 특징 학습 ]
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(256, activation='relu'), # Dense : 완전 연결된 신경망 층, 이전 node(뉴런) 받아서 패턴 학습 한다.
        # 주로 노드 개수는 32 64 128 사용한다.
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(1, activation='sigmoid'),
    ])
    return model
model = build_model()
# 모델 컴파일
model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001), loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])
# 모델 훈련
history = model.fit(train_gen,
                    validation_data=valid_gen,
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
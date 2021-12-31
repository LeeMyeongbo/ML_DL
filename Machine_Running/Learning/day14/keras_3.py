import matplotlib.pyplot as plt
import keras
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Dropout

# 데이터 변수 선언
num_classes = 10
im_rows = 32
im_cols = 32
im_size = im_rows * im_cols * 3  # RGB 컬러 이미지

# 1. 데이터 읽어 들이기
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# 2. 데이터 가공
# 3차원 변환 및 정규화
x_train = x_train.reshape(-1, im_size).astype('float32') / 255
x_test = x_test.reshape(-1, im_size).astype('float32') / 255
# 레이블 데이터를 one-hot Encoding 형식으로 변환
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# 3. ANN 모델 정의
model = Sequential()
# 1번째 레이어 : 입력층 -> 입력 데이터 크기 가정
model.add(Dense(512, activation='relu', input_shape=(im_size,)))  # 입력층
# 마지막 레이어 : 출력층
model.add(Dense(num_classes, activation='softmax'))

# 4. 모델 생성
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 5. 학습 실행하기
# 전체 데이터 반복 횟수 : epoch -> 50
# 전체 데이터 1회 반복 시 학습 데이터 크기 : 32
hist = model.fit(x_train, y_train, batch_size=32, epochs=50, verbose=1, validation_data=(x_test, y_test))

# 6. 모델 평가하기
score = model.evaluate(x_test, y_test, verbose=1)
print('정답률 =', score[1], 'loss =', score[0])

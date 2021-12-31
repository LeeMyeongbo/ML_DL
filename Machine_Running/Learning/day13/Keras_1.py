import tensorflow.contrib.keras as ke
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# 1. 데이터 준비 - 분꽃 데이터 읽어 들이고 레이블과 입력 데이터로 분리
iris_data = pd.read_csv('./iris.csv', encoding='utf-8')
y_label = iris_data.iloc[:, -1]  # iris name 라벨
x_data = iris_data.iloc[:, :-1]  # iris name 라벨을 제외한 4가지 구분 데이터

labels = {'setosa': [1, 0, 0], 'versicolor': [0, 1, 0], 'virginica': [0, 0, 1]}
y_nums = np.array(list(map(lambda v: labels[v], y_label)))
x_train, x_test, y_train, y_test = train_test_split(x_data, y_nums, train_size=0.8)

# 2. 모델 구조 정의
Dense = ke.layers.Dense
model = ke.models.Sequential()
model.add(Dense(10, activation='relu', input_shape=(4, )))
model.add(Dense(3, activation='softmax'))

# 모델 구축
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 3. 학습 실행하기
model.fit(x_train, y_train, batch_size=20, epochs=300)

# 4. 모델 평가
score = model.evaluate(x_test, y_test, verbose=1)
print('정답률 =', score[1], 'loss =', score[0])

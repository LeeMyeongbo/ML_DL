import tensorflow as tf

num_classes = 10                    # 출력 클래스의 개수

def Make_Data():
    # 데이터를 학습 데이터와 테스트 데이터로 나눈다.
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # 입력 이미지를 2차원에서 1차원 벡터로 변경한다.
    x_train = x_train.reshape(60000, 784)
    x_test = x_test.reshape(10000, 784)

    # 입력 이미지의 픽셀 값이 0.0에서 1.0 사이의 값이 되게 한다.
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    y_train = tf.keras.utils.to_categorical(y_train, num_classes)
    y_test = tf.keras.utils.to_categorical(y_test, num_classes)

    return x_train, y_train, x_test, y_test

def Set_Neural_Network_Model():
    # 신경망의 모델을 구축한다.
    model = tf.keras.models.Sequential()
    model.add(tf.keras.Input(shape=(784,)))
    model.add(tf.keras.layers.Dense(256, activation='relu'))
    model.add(tf.keras.layers.Dense(num_classes, activation='relu'))
    model.summary()
    sgd = tf.keras.optimizers.SGD(lr=0.01)

    # 손실 함수를 제곱 오차 함수로 설정하고 학습 알고리즘은 SGD 방식으로 한다.
    model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

    return model


X_train, Y_train, X_test, Y_test = Make_Data()
Model = Set_Neural_Network_Model()

# 학습을 수행한다.
history = Model.fit(X_train, Y_train, batch_size=128, epochs=50)

# 학습을 평가한다.
score = Model.evaluate(X_test, Y_test, verbose=0)
print('테스트 손실값:', score[0])
print('테스트 정확도:', score[1])

# 학습시킨 모델의 파라미터를 저장한다.
Model.save('mnist_mlp_model.h5')

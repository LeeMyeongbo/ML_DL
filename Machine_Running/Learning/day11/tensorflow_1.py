import tensorflow as tf

# 노드 정의
# 선형회귀 모델 (Wx + b) 정의
W = tf.Variable(tf.random_normal(shape=[1]))
b = tf.Variable(tf.random_normal(shape=[1]))
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# 선형회귀 모델 연산 정의
linear_model = W * x + b
loss = tf.reduce_mean(tf.square(linear_model - y))  # 손실 함수 정의

# 최적화 그라디언트 디센트 / 러닝 레이트 => 학습 속도 설정
optimizer = tf.train.GradientDescentOptimizer(0.01)
train_step = optimizer.minimize(loss)

# 트레이닝을 위한 입력값과 출력값을 준비
x_train = [1, 2, 3, 4]
y_train = [2, 4, 6, 8]

# 2. 세션 실행, 파라미터 추출한 임의의 값으로 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())  # random_normal() 임의의 값 할당

# 3. 모델 학습 실행 : 경사하강법을 1000번 실행
for i in range(1000):
    sess.run(train_step, feed_dict={x: x_train, y: y_train})  # 학습데이터 지정 및 학습
    print(i, sess.run(W), sess.run(b))

# 4. 테스트 진행
x_test = [3.5, 5, 5.5, 6]
print(sess.run(linear_model, feed_dict={x: x_test}))  # 예상되는 참값 : [7, 10, 11, 12]

# 5. 세션 종료
sess.close()

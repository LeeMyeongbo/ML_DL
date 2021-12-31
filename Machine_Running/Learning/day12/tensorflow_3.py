import tensorflow as tf

# MNIST 데이터 다운로드
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./datas/", one_hot=True)

# 입력값 & 출력값을 받기 위한 플레이스홀더 정의
x = tf.placeholder(tf.float32, shape=[None, 784])  # 28 * 28
y = tf.placeholder(tf.float32, shape=[None, 10])  # 정답이 0 ~ 9

# 변수 설정 및 sotfmax regression 모델 정의
W = tf.Variable(tf.zeros(shape=[784, 10]))
b = tf.Variable(tf.zeros(shape=[10]))
logits = tf.matmul(x, W) + b  # 자원 축소 4 => 3
y_pred = tf.nn.softmax(logits)  # 출력 차원별 확률로 변환

# cross-entropy 손실 함수와 옵티마이저 정의
# 출력 N차원으로 N차원 값 합 & 평균
loss = tf.reduce_mean(-tf.reduce_sum(y * tf.log(y_pred), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

# 세션을 열고 변수들에 초기값을 할당
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 1000번 반복을 수행하면서 최적화를 수행
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)  # 지정된 크기만큼 데이터 가져옴
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

# 학습이 끝나면 학습된 모델의 정확도 출력
correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('정확도 : %f' % sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))  # 정확도 약 91%
sess.close()

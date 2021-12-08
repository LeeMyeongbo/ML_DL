
# =========================== 로드된 데이터를 입력으로 넣어 학습을 시작합니다. ===========================
"""
ID: 2017113888
NAME: Lee Myeongbo
OS: Ubuntu 18.10
Python version: 3.8.12
"""

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import time                 # 실행시간 측정
from common.deep_convnet import DeepConvNet
from common.trainer import Trainer
from datapreparation import load_data

epochs = 10
learning_rate = 0.001
start = time.time()
x_train, t_train, x_test, t_test = load_data()      # data 로드(이미지가 변환된 배열 및 정답 레이블 가져오기)
network = DeepConvNet()                             # 모델 구조=심층 CNN
trainer = Trainer(network, x_train, t_train, x_test, t_test, epochs, batch_size=30, eval_size=30, 
                  optimizer='Adam', param={'lr':learning_rate})
trainer.train()             # 학습 시작

# 모델 보관
lr = str(learning_rate).replace('.', '_')
network.save_params('epoch=' + str(epochs) + ', lr=' + lr + '.pkl')
print("Saved Network Parameters!")

# 학습 소요 시간 표시
t = time.time() - start
print("elapsed time : {0}h {1}m {2}s".format(int(t // 3600), int(t % 3600 // 60), int(t % 3600 % 60)))

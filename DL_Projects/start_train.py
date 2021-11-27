# -*- coding: utf-8 -*-
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

epochs = 5
learning_rate = 0.001
start = time.time()
x_train, t_train, x_val, t_val, x_test, t_test = load_data()
network = DeepConvNet()
trainer = Trainer(network, x_train, t_train, x_val, t_val, x_test, t_test, epochs, batch_size=60, val_batch_size=70, 
                  optimizer='Adam', param={'lr':learning_rate})
trainer.train()

# 매개변수 보관
lr = str(learning_rate).replace('.', '_')
network.save_params('epoch=' + str(epochs) + ', lr=' + lr + '.pkl')
print("Saved Network Parameters!")

t = time.time() - start
print(" elapsed time : {0}h {1}m {2}s".format(int(t // 3600), int(t % 3600 // 60), int(t % 3600 % 60)))

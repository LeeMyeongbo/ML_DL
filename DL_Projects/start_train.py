# -*- coding: utf-8 -*-
"""
ID: 2017113888
NAME: Lee Myeongbo
OS: Ubuntu 18.10
Python version: 3.8.1
"""

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import time                 # 실행시간 측정
from common.deep_convnet import DeepConvNet
from common.trainer import Trainer
from datapreparation import load_data

start = time.time()
x_train, t_train, x_val, t_val, x_test, t_test = load_data()
network = DeepConvNet()
trainer = Trainer(network, x_train, t_train, x_val, t_val, x_test, t_test, epochs=1, batch_size=30, iter_samples=30, 
                  optimizer='Adam', param={'lr':0.001})

trainer.train()

# 매개변수 보관
network.save_params("deep_convnet_params.pkl")
print("Saved Network Parameters!")
print("time :", time.time() - start)

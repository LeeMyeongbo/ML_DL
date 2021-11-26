# -*- coding: utf-8 -*-
"""
ID: 20210910
NAME: Python Programming Review
OS: Ubuntu 18.10
Python version: 3.6.9
"""

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import matplotlib.pyplot as plt
from common.deep_convnet import DeepConvNet
from datapreparation import load_data

x_train, t_train, x_val, t_val, x_test, t_test = load_data()
network = DeepConvNet()
network.load_params("deep_convnet_params.pkl")

print("calculating test accuracy ... ")

classified_ids = []
acc = 0.0
batch_size = 20

for i in range(int(x_test.shape[0] / batch_size)):
    tx = x_test[i*batch_size:(i+1)*batch_size]
    tt = t_test[i*batch_size:(i+1)*batch_size]
    y = network.predict(tx, train_flg=False)
    y = np.argmax(y, axis=1)
    classified_ids.append(y)
    acc += np.sum(y == tt)

acc = acc / x_test.shape[0]
print("test accuracy:" + str(acc))

classified_ids = np.array(classified_ids)
classified_ids = classified_ids.flatten()

current_view = 1
mis_pairs = {}
for i, val in enumerate(classified_ids == t_test):
    if not val:
        result = x_test[i].transpose((1,2,0)) * 255.0
        result = result.astype('uint8')
        plt.imshow(result)
        plt.axis('off')
        plt.show()
        mis_pairs[current_view] = (t_test[i], classified_ids[i])
        
        current_view += 1

print("======= misclassified result =======")
print("{view index: (label, inference), ...}")
print(mis_pairs)

# -*- coding: utf-8 -*-
"""
ID: 2017113888
NAME: Lee Myeongbo
OS: Ubuntu 18.10
Python version: 3.8.12
"""

import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import PIL.Image as Image
from urllib.request import urlretrieve
from zipfile import ZipFile

train_bpath = 'SCDataset/train/benign/'
train_mpath = 'SCDataset/train/malignant/'
test_bpath = 'SCDataset/test/benign/'
test_mpath = 'SCDataset/test/malignant/'


def prepare(path, imgs, label, size):
    x = np.empty(shape=(size, 3, 224, 224))
    t = np.empty(shape=(size,)).astype(int)
    
    for i in range(len(imgs)):
        img = Image.open(path + imgs[i])
        img_array = np.array(img).transpose((2,0,1))
        x[i] = img_array
        t[i] = label
    
    # data argumentation -- 원래 input data set에 변형을 가해서 데이터 추가
    rotated_img_index = np.random.choice(len(imgs), size - len(imgs), replace=False)    # (size-원래 이미지 수)만큼의 데이터 추가
    for i in range(size - len(imgs)):
        img = Image.open(path + imgs[rotated_img_index[i]])
        degree = 90 * np.random.randint(1, 4)                                           # 90, 180, 270 중 택 1
        r_img = img.rotate(degree)                                                      # 선택한 각도만큼 돌림
        r_img.save(path + 'r_' + imgs[rotated_img_index[i]])                            # 돌린 이미지 저장
        img_array = np.array(r_img).transpose((2,0,1))
        x[len(imgs) + i] = img_array
        t[len(imgs) + i] = label
        
    x /= 255.0
    return (x, t)


def load_data():
    if not os.path.exists('SCDataset'):
        urlretrieve('https://media.githubusercontent.com/media/LeeMyeongbo/Datasets/main/SCDataset.zip', 'SCDataset.zip')
        with ZipFile('SCDataset.zip', 'r') as z:
            z.printdir()
            z.extractall()
    
    train_bimgs = os.listdir(train_bpath)
    train_mimgs = os.listdir(train_mpath)
    test_bimgs = os.listdir(test_bpath)
    test_mimgs = os.listdir(test_mpath)
    
    (x_btrain, t_btrain) = prepare(train_bpath, train_bimgs, 0, 450)
    (x_mtrain, t_mtrain) = prepare(train_mpath, train_mimgs, 1, 450)
    (x_btest, t_btest) = prepare(test_bpath, test_bimgs, 0, len(test_bimgs))
    (x_mtest, t_mtest) = prepare(test_mpath, test_mimgs, 1, len(test_mimgs))
    
    x_train = np.concatenate((x_btrain, x_mtrain), axis=0)
    t_train = np.concatenate((t_btrain, t_mtrain), axis=0)
    x_test = np.concatenate((x_btest, x_mtest), axis=0)
    t_test = np.concatenate((t_btest, t_mtest), axis=0)
    
    return x_train, t_train, x_test, t_test

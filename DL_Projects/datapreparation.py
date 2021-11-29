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
    
    for i in range(size):
        img = Image.open(path + imgs[i])
        img_array = np.array(img).transpose((2,0,1))
        x[i] = img_array
        t[i] = label
    
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
    
    (x_btrain, t_btrain) = prepare(train_bpath, train_bimgs, 0, len(train_bimgs))
    (x_mtrain, t_mtrain) = prepare(train_mpath, train_mimgs, 1, len(train_mimgs))
    (x_btest, t_btest) = prepare(test_bpath, test_bimgs, 0, len(test_bimgs))
    (x_mtest, t_mtest) = prepare(test_mpath, test_mimgs, 1, len(test_mimgs))
    
    x_train = np.concatenate((x_btrain, x_mtrain), axis=0)
    t_train = np.concatenate((t_btrain, t_mtrain), axis=0)
    x_test = np.concatenate((x_btest, x_mtest), axis=0)
    t_test = np.concatenate((t_btest, t_mtest), axis=0)
    
    return x_train, t_train, x_test, t_test

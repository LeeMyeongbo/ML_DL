
# =========================== 이미지 데이터를 다운로드 받고 전처리한 다음 배열에 저장합니다. ===========================
"""
ID: 2017113888
NAME: Lee Myeongbo
OS: Ubuntu 18.10
Python version: 3.8.12
"""

import os
import sys

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
    x = np.empty(shape=(size, 3, 224, 224))                 # 이미지 데이터 저장용 배열
    t = np.empty(shape=(size,)).astype(int)                 # 정답 레이블 (실수형이 아닌 정수형으로 지정)
    
    for i in range(len(imgs)):
        img = Image.open(path + imgs[i])                    # 경로 내 이미지 파일 오픈
        img_array = np.array(img).transpose((2,0,1))        # (세로픽셀수*가로픽셀수*채널) -> (채널*세로픽셀수*가로픽셀수)로 축 변환
        x[i] = img_array
        t[i] = label
    
    # data augmentation -- 원래 train dataset에 변형을 가해서 데이터 추가
    rotated_img_index = np.random.choice(len(imgs), size - len(imgs), replace=False)    # (size-원래 이미지 수)만큼의 데이터 추가
    for i in range(size - len(imgs)):
        img = Image.open(path + imgs[rotated_img_index[i]])
        degree = 90 * np.random.randint(1, 4)                                           # 90, 180, 270 중 택 1
        r_img = img.rotate(degree)                                                      # 선택한 각도만큼 돌림
        r_img.save(path + 'r_' + imgs[rotated_img_index[i]])                            # 돌린 이미지 저장
        img_array = np.array(r_img).transpose((2,0,1))
        x[len(imgs) + i] = img_array
        t[len(imgs) + i] = label
        
    x /= 255.0                                              # 0 ~ 255 의 값을 0 ~ 1로 변환
    return (x, t)


def load_data():
    if not os.path.exists('SCDataset'):                     # 데이터가 없다면 다운로드
        urlretrieve('https://media.githubusercontent.com/media/LeeMyeongbo/Datasets/main/SCDataset.zip', 'SCDataset.zip')
        with ZipFile('SCDataset.zip', 'r') as z:
            z.printdir()
            z.extractall()                                  # 즉시 압축 풀기
    
    train_bimgs = os.listdir(train_bpath)                   # train 폴더 내 benign에 있는 이미지 파일 리스트
    train_mimgs = os.listdir(train_mpath)                   # train 폴더 내 malignant에 있는 이미지 파일 리스트
    test_bimgs = os.listdir(test_bpath)                     # test 폴더 내 benign에 있는 이미지 파일 리스트
    test_mimgs = os.listdir(test_mpath)                     # test 폴더 내 malignant에 있는 이미지 파일 리스트
    
    (x_btrain, t_btrain) = prepare(train_bpath, train_bimgs, 0, 450)            # benign은 0으로 labeling
    (x_mtrain, t_mtrain) = prepare(train_mpath, train_mimgs, 1, 450)            # malignant는 1로 labeling
    (x_btest, t_btest) = prepare(test_bpath, test_bimgs, 0, len(test_bimgs))    # test dataset도 마찬가지로 적용
    (x_mtest, t_mtest) = prepare(test_mpath, test_mimgs, 1, len(test_mimgs))
    
    x_train = np.concatenate((x_btrain, x_mtrain), axis=0)
    t_train = np.concatenate((t_btrain, t_mtrain), axis=0)
    x_test = np.concatenate((x_btest, x_mtest), axis=0)
    t_test = np.concatenate((t_btest, t_mtest), axis=0)
    
    return x_train, t_train, x_test, t_test

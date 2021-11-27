# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import common.optimizer as op
import matplotlib.pyplot as plt


class Trainer:              # 신경망 훈련 시킴
    def __init__(self, network, x_train, t_train, x_val, t_val, x_test, t_test, epochs, batch_size, val_batch_size,
                 optimizer, param={'lr':0.001}):
        self.network = network
        self.x_train = x_train
        self.t_train = t_train
        self.x_val = x_val
        self.t_val = t_val
        self.x_test = x_test
        self.t_test = t_test
        self.epochs = epochs
        self.batch_size = batch_size
        self.train_size = x_train.shape[0]
        self.val_size = x_val.shape[0]
        self.val_batch_size = val_batch_size
        self.iter_per_epoch = max(self.train_size // batch_size, 1)
        self.iter_per_val = max(self.val_size // val_batch_size, 1)
        self.train_loss_list = []
        self.train_acc_list = []
        self.val_loss_list = []
        self.val_acc_list = []
        optimizer_class_dict = {'sgd':op.SGD, 'momentum':op.Momentum, 'nesterov':op.Nesterov, 'adagrad':op.AdaGrad, 
                                'rmsprpo':op.RMSprop, 'adam':op.Adam}
        self.optimizer = optimizer_class_dict[optimizer.lower()](**param)


    def train(self):
        train_seq = np.arange(self.train_size)
        val_seq = np.arange(self.val_size)
        
        for i in range(self.epochs):                        # 전체 데이터 학습 반복 횟수
            print("================== epoch " + str(i+1) + " ==================")
            
            np.random.shuffle(train_seq)
            train_loss_tmp = []
            train_acc_tmp = []
            
            for j in range(self.iter_per_epoch):            # 전체 데이터를 몇 개(=batch size)로 나눠서 학습하는가
                x_batch = self.x_train[train_seq[self.batch_size*j:self.batch_size*(j+1)]]
                t_batch = self.t_train[train_seq[self.batch_size*j:self.batch_size*(j+1)]]
                
                grads = self.network.gradient(x_batch, t_batch)
                self.optimizer.update(self.network.params, grads)
                
                train_loss = self.network.loss(x_batch, t_batch)
                train_loss_tmp.append(train_loss)
                train_acc = self.network.accuracy(x_batch, t_batch, batch_size=self.batch_size)
                train_acc_tmp.append(train_acc)
                print('epoch ' + str(i+1) + '-' + str(j+1) + ' completed')
                
            np.random.shuffle(val_seq)
            val_loss_tmp = []
            val_acc_tmp = []
            
            for j in range(self.iter_per_val):
                x_val_batch = self.x_val[val_seq[self.val_batch_size*j:self.val_batch_size*(j+1)]]
                t_val_batch = self.t_val[val_seq[self.val_batch_size*j:self.val_batch_size*(j+1)]]
                
                val_loss = self.network.loss(x_val_batch, t_val_batch)
                val_loss_tmp.append(val_loss)
                val_acc = self.network.accuracy(x_val_batch, t_val_batch, batch_size=self.val_batch_size)
                val_acc_tmp.append(val_acc)
            
            train_loss_avg = sum(train_loss_tmp) / self.iter_per_epoch
            self.train_loss_list.append(train_loss_avg)
            train_acc_avg = sum(train_acc_tmp) / self.iter_per_epoch
            self.train_acc_list.append(train_acc_avg)
            
            val_loss_avg = sum(val_loss_tmp) / self.iter_per_val
            self.val_loss_list.append(val_loss_avg)
            val_acc_avg = sum(val_acc_tmp) / self.iter_per_val
            self.val_acc_list.append(val_acc_avg)

            print("\ntrain_loss:" + str(train_loss_avg) + ", train_acc:" + str(train_acc_avg))
            print("val_loss:" + str(val_loss_avg) + ", val_acc:" + str(val_acc_avg) + '\n')

        test_acc = self.network.accuracy(self.x_test, self.t_test, batch_size=self.batch_size)

        print("================== Final Test Accuracy ==================")
        print("test_acc:" + str(test_acc))

        plt.xlabel('epochs')
        plt.xticks(np.arange(1, self.epochs + 1))
        plt.plot(np.arange(1, self.epochs + 1), self.train_loss_list, 'b', label='train_loss', linewidth=0.5)
        plt.plot(np.arange(1, self.epochs + 1), self.train_acc_list, 'y', label='train_acc', linewidth=0.5)
        plt.plot(np.arange(1, self.epochs + 1), self.val_loss_list, 'g', label='val_loss', linewidth=0.5)
        plt.plot(np.arange(1, self.epochs + 1), self.val_acc_list, 'r', label='val_acc', linewidth=0.5)
        plt.legend(loc=(0, 1.01), fontsize=8, ncol=4)
        plt.show()

# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import common.optimizer as op
import matplotlib.pyplot as plt


class Trainer:              # 신경망 훈련 시킴
    def __init__(self, network, x_train, t_train, x_val, t_val, x_test, t_test, epochs, batch_size, iter_samples,
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
        self.iter_samples = iter_samples
        self.iter_per_epoch = max(self.train_size // batch_size, 1)
        self.train_loss_list = []
        self.val_loss_list = []
        self.val_acc_list = []
        
        optimizer_class_dict = {'sgd':op.SGD, 'momentum':op.Momentum, 'nesterov':op.Nesterov, 'adagrad':op.AdaGrad, 
                                'rmsprpo':op.RMSprop, 'adam':op.Adam}
        self.optimizer = optimizer_class_dict[optimizer.lower()](**param)


    def train(self):
        train_seq = np.arange(self.train_size)
        
        for i in range(self.epochs):                        # 전체 데이터 학습 반복 횟수
            np.random.shuffle(train_seq)
            train_loss_tmp = []
            
            for j in range(self.iter_per_epoch):            # 전체 데이터를 몇 개(=batch size)로 나눠서 학습하는가
                x_batch = self.x_train[train_seq[self.batch_size*j:self.batch_size*(j+1)]]
                t_batch = self.t_train[train_seq[self.batch_size*j:self.batch_size*(j+1)]]
                
                grads = self.network.gradient(x_batch, t_batch)
                self.optimizer.update(self.network.params, grads)
                
                train_loss = self.network.loss(x_batch, t_batch)
                train_loss_tmp.append(train_loss)
                
                print('epoch ' + str(i+1) + '-' + str(j+1) + ' completed')
            
            batch_sample = np.random.choice(len(self.t_val), self.iter_samples, replace=False)
            
            x_val_sample = self.x_val[batch_sample]
            t_val_sample = self.t_val[batch_sample]
            
            train_loss_avg = sum(train_loss_tmp) / len(train_loss_tmp)
            self.train_loss_list.append(train_loss_avg)
            val_loss = self.network.loss(x_val_sample, t_val_sample)
            self.val_loss_list.append(val_loss)
            val_acc = self.network.accuracy(x_val_sample, t_val_sample, batch_size=self.batch_size)
            self.val_acc_list.append(val_acc)

            print("=== epoch:" + str(i+1) + ", train_loss:" + str(train_loss_avg) + 
                  ", val_loss:" + str(val_loss) + ", val_acc:" + str(val_acc) + " ===")

        test_acc = self.network.accuracy(self.x_test, self.t_test, batch_size=self.batch_size)

        print("=============== Final Test Accuracy ===============")
        print("test_acc:" + str(test_acc))
        
        plt.xlabel('epochs')
        plt.plot(np.arange(self.epochs) + 1, self.train_loss_list, 'b', label='train_loss', linewidth=0.5)
        plt.plot(np.arange(self.epochs) + 1, self.val_loss_list, 'g', label='val_loss', linewidth=0.5)
        plt.plot(np.arange(self.epochs) + 1, self.val_acc_list, 'r', label='val_acc', linewidth=0.5)
        plt.legend(loc=(0, 1.01), fontsize=8, ncol=3)
        plt.show()

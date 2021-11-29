# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import common.optimizer as op
import matplotlib.pyplot as plt


class Trainer:              # 신경망 훈련 시킴
    def __init__(self, network, x_train, t_train, x_test, t_test, epochs, batch_size, eval_size, optimizer, param={'lr':0.001}):
        self.network = network
        self.x_train = x_train
        self.t_train = t_train
        self.x_test = x_test
        self.t_test = t_test
        self.epochs = epochs
        self.batch_size = batch_size
        self.train_size = x_train.shape[0]
        self.test_size = x_test.shape[0]
        self.eval_size = eval_size
        self.iter_per_epoch = max(self.train_size // batch_size, 1)
        self.train_loss_list = []
        self.train_acc_list = []
        self.test_loss_list = []
        self.test_acc_list = []
        optimizer_class_dict = {'sgd':op.SGD, 'momentum':op.Momentum, 'nesterov':op.Nesterov, 'adagrad':op.AdaGrad, 'rmsprpo':op.RMSprop, 'adam':op.Adam}
        self.optimizer = optimizer_class_dict[optimizer.lower()](**param)


    def train(self):
        train_seq = np.arange(self.train_size)
        
        for i in range(self.epochs):                        # 전체 데이터 학습 반복 횟수
            print("\n================== epoch " + str(i+1) + " ==================")
            
            train_loss_avg = 0.0
            np.random.shuffle(train_seq)
            for j in range(self.iter_per_epoch):            # 전체 데이터를 몇 개(=batch size)로 나눠서 학습하는가
                x_batch = self.x_train[train_seq[self.batch_size*j:self.batch_size*(j+1)]]
                t_batch = self.t_train[train_seq[self.batch_size*j:self.batch_size*(j+1)]]
                
                grads = self.network.gradient(x_batch, t_batch)
                self.optimizer.update(self.network.params, grads)
                
                train_loss = self.network.loss(x_batch, t_batch)
                train_loss_avg += train_loss
                
                print(str(j+1) + ": train_loss=" + str(train_loss))
            
            train_loss_avg /= self.iter_per_epoch
            self.train_loss_list.append(train_loss_avg)
            train_acc = self.network.accuracy(self.x_train, self.t_train, self.batch_size)
            self.train_acc_list.append(train_acc)
            
            test_sample_idx = np.random.choice(self.test_size, self.eval_size)
            x_test_sample = self.x_test[test_sample_idx]
            t_test_sample = self.t_test[test_sample_idx]
            
            test_loss = self.network.loss(x_test_sample, t_test_sample)
            self.test_loss_list.append(test_loss)
            test_acc = self.network.accuracy(x_test_sample, t_test_sample, self.eval_size)
            self.test_acc_list.append(test_acc)
            
            print("\nevaluation " + str(i+1) + ": train_loss=" + str(train_loss_avg) + ", test_loss=" + str(test_loss) + ", test_acc=" + str(test_acc))

        print("\n================== Final Test Accuracy ==================")
        test_acc = self.network.accuracy(self.x_test, self.t_test)
        print("test_acc:" + str(test_acc))
        
        plt.xlabel('epochs')
        plt.xticks(np.arange(1, self.epochs + 1))
        plt.plot(np.arange(1, self.epochs + 1), self.train_loss_list, 'b', label='train_loss', linewidth=0.5)
        plt.plot(np.arange(1, self.epochs + 1), self.train_acc_list, 'b', label='train_acc', linewidth=0.5)
        plt.plot(np.arange(1, self.epochs + 1), self.test_loss_list, 'g', label='test_loss', linewidth=0.5)
        plt.plot(np.arange(1, self.epochs + 1), self.test_acc_list, 'r', label='test_acc', linewidth=0.5)
        plt.legend(loc=(0, 1.01), fontsize=8, ncol=4)
        plt.show()

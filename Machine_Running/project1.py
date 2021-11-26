# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def calculate(input):
    global weights
    global bias
    activation = bias
    
    for i in range(2):
        activation += weights[i] * input[i]
    
    if activation >= 0.0:
        return 1.0
    else:
        return 0.0
    

def train_weights(X, y, l_rate, n_epoch):
    global weights
    global bias
    
    for epoch in range(n_epoch):
        sum_error = 0.0
        
        for row, target in zip(X, y):
            actual = calculate(row)
            error = target - actual
            bias += l_rate * error
            sum_error += error**2
            
            for i in range(2):
                weights[i] += l_rate * error * row[i]
            print(weights, bias)
        print('에포크=%d, 학습률=%.3f, 오류=%.3f' % (epoch, l_rate, sum_error))
        
        plt.axis([-0.5, 1.5, -0.5, 1.5])
        plt.scatter(0, 0, color='red')
        plt.scatter(0, 1, color='blue')
        plt.scatter(1, 0, color='blue')
        plt.scatter(1, 1, color='blue')
        
        graph_x = np.arange(-10, 10, 0.1)
        graph_y = [-1 * weights[0] / weights[1] * n + (-1 * bias / weights[1]) for n in graph_x]
        plt.plot(graph_x, graph_y)
        plt.show()
        
    return weights

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 1]

weights = [0.0, 0.0]
bias = 0.0

l_rate = 0.1
n_epoch = 5
weights = train_weights(X, y, l_rate, n_epoch)

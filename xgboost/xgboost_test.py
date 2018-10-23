#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pdb

#### one-hot encode #####
enc = preprocessing.OneHotEncoder()
enc.fit([[0,1,3],[0,1,0],[0,2,1],[1,0,2]])
array = enc.transform([[0,1,3]]).toarray()
print(array)
print(len(array))


def iris_xgboost():
    """
    这里主要解释以下param的设置，objective设置的是你的分类的目标及方法，除了我们用的多分类的multi:softmax，还可以是binary:logistic，reg:logistic等等，根据你的目标需要去设置。
    eta设置的是衰减因子，就是在步长前面乘以一个系数，设置过小容易导致计算时间太长，太大又很容易过拟合，
    max_depth是所用的树的最大深度，
    silent是打印运行信息，没什么太大的意义，
    num_class应该是类的数目吧，
    nthread是调用的线程数，
    num_round是迭代计算次数。
    
    """
    iris = datasets.load_iris()  # sklearn的datasets里面已经包含了iris数据集
    x = iris.data[:,:2]  # 取前两列
    # print(x)
    # pdb.set_trace()
    y = iris.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, random_state=1)
    data_train = xgb.DMatrix(x_train, label=y_train)
    data_test = xgb.DMatrix(x_test, label=y_test)
    param = {}
    param['objective'] = 'multi:softmax'
    param['eta'] = 0.1
    param['max_depth'] = 6
    param['silent'] = 1
    param['nthread'] = 4
    param['num_class'] = 3
    watchlist = [ (data_train, 'train'), (data_test, 'test') ]
    num_round = 10
    bst = xgb.train(param, data_train, num_round, watchlist)
    print(bst)  # <xgboost.core.Booster object at 0x000002A4184ED4E0>
    pred = bst.predict(data_test)
    print(pred)
    print ('predicting, classification error=%f' % (sum( int(pred[i]) != y_test[i] for i in range(len(y_test))) / float(len(y_test)) ))

# if __name__ == '__main__':
#     iris_xgboost()
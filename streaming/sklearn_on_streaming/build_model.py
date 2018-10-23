#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pdb
import pickle


def build():
    iris = load_iris()
    samples = iris.data
    out_samples = samples.astype(np.float64)
    # print(samples)
    # print(samples.dtype)
    # # np.savetxt('iris.txt', out_samples)
    # pdb.set_trace()

    target = iris.target
    # print(target)
    # pdb.set_trace()

    classifier = LogisticRegression()
    classifier.fit(samples, target)

    test = np.array([5, 3, 5, 2.5])
    test = test.reshape(1, -1)

    y = classifier.predict(test)
    prob = classifier.predict_proba(test)
    # print(y)
    # print(prob)

    # s = np.sum(prob)
    # print(s)

    # pickle
    with open('lr.pkl', 'wb') as fw:
        pickle.dump(classifier, fw)


def test(model_path):
    test = np.array([5, 3, 5, 2.5])
    test = test.reshape(1, -1)
    with open(model_path, 'rb') as f:
        lr = pickle.load(f)
        y = lr.predict(test)
        print(y)


def test_2(model_path, test_data):
    test_data = np.loadtxt(test_data)
    # print(test_data.dtype)
    with open(model_path, 'rb') as f:
        lr = pickle.load(f)
        y = lr.predict(test_data)
        print(y)


if __name__ == '__main__':
    # build()

    model_path = './lr.pkl'
    # test(model_path)
    test_data ='./iris.txt'
    test_2(model_path, test_data)


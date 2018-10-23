#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import random


def test_multiply():
    a = np.array([1,2,3,4,5,6])
    b = np.array([1,0,1,0,0,1])
    c = a * (b > 0)
    print(c)

###############################
'''stack：感觉就是axis从0每次加1，就把一列里面的所有元素拿出来放成一行'''
def test_stack_1():
    '''stack： 1 dimension to 2 dimension'''
    a = [[1,2,3,4], [5,6,7,8]]
    print('original: ', a)
    b = np.stack(a, axis=0)
    print('b: ', b)
    c = np.stack(a, axis=1)
    print('c: ', c)
    ### error
    # d = np.stack(a, axis=2)
    # print('d: ', d)

def test_stack_2():
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = [9,10,11,12]
    d = np.stack((a,b,c), axis=0)
    print('d: ', d)
    e = np.stack((a,b,c), axis=1)
    print('e: ', e)

def test_stack_3():
    '''stack: 2 dimension to 3 dimension'''
    a = [[1,2,3], [4,5,6]]
    b = [[1,2,3], [4,5,6]]
    c = [[1,2,3], [4,5,6]]
    print("增加一维，新维度的下标为0")
    d = np.stack((a,b,c),axis=0)
    print(d)
    print("增加一维，新维度的下标为1")
    d = np.stack((a,b,c),axis=1)
    print(d)
    print("增加一维，新维度的下标为2")
    d = np.stack((a,b,c),axis=2)
    print(d)

#################################
def test_hstack():
    '''函数原型：hstack(tup) ，参数tup可以是元组，列表，或者numpy数组，返回结果为numpy的数组'''
    a = [1,2,3]
    b = [4,5,6]
    c = np.hstack((a,b))
    print(c)


def test_ones():
    a = np.ones(5)
    b = np.ones((2,5))
    print('a: ', a)
    print('b: ', b)
    c = np.matrix(np.ones((3,6)))
    print('matrix of ones: ', c)


def test_sum():
    a = np.ones((3,5))
    a[1, 3] = random.random()
    print('original: ', a)
    b = np.sum(a, axis=0)
    print('sum of cols: ', b)
    c = np.sum(a, axis=1)
    print('sum of rows: ', c)

if __name__ == '__main__':
    # test_multiply()
    # test_stack_1()
    # test_stack_2()
    # test_stack_3()
    # test_hstack()
    # test_ones()
    test_sum()
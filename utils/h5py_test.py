#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
h5py is a Pythonic interface to the HDF5 binary data format.
HDF5 lets us store huge amounts of numerical data, and easily manipulate that data from Numpy.
'''

import h5py
import numpy as np


def createFile(file_path):
    with h5py.File(file_path, 'w') as f:
        dset = f.create_dataset('h5py_test', (100,), dtype='i')


def createFile_2(file_path):
    imgData = np.ones((30,3,128,256))  # 最里层是128*256矩阵，外一层是2*(128*256)，再外一层是3*(2*(128*256))
    f = h5py.File(file_path, 'w')  # 创建一个h5文件并且为写模式
    f['data'] = imgData  # 将数据写入文件的主键data下面
    f['label'] = range(100)  # 将数据写入文件的主键labels下面
    f.close()  # 不是with打开的需要手动close掉


def readFile(file_path):
    f = h5py.File(file_path, 'r')
    print('keys: ', f.keys())
    # print(f['data'][:])
    print(f['label'][:])
    f.close()



if __name__ == '__main__':
    file_path_1 = '../test_files/h5py_test.hdf5'
    # createFile(file_path_!)
    
    file_path_2 = '../test_files/h5py_test_2.hdf5'
    # createFile_2(file_path_2)
    readFile(file_path_2)
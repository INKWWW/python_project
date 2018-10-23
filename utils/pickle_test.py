#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''pickle 序列化'''

import pickle

a_dict = {'da':111, 2:[23,4,1], '23':{1:2, 'd':'dad'}}

# store
file = open('pickle_ex.pickle', 'wb')
pickle.dump(a_dict, file)  # 序列化 a_dict到打开的文件file中
file.close()

# read
file = open('pickle_ex.pickle', 'rb')
a_dict1 = pickle.load(file)  # 读取打开的序列化文件file
file.close()
print(a_dict1)

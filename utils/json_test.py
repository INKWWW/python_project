#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

'''
1、loads & dumps 都是针对内存中的变量进行操作的。dumps--序列化，loads--反序列化
2、load & dump 都是针对文件句柄的，就是对json文件进行操作的
'''

a = {'x':1, 'y':2, 'z':True}

# dumps读取内存中的变量，序列化为str
a_dumps = json.dumps(a)
print('--------dumps--------')
print(a_dumps)  # {"x": 1, "y": 2, "z": true} - 注意：单引号变双引号；True变成true
print(type(a_dumps))  # str

# loads 反序列化str为dict
a_loads = json.loads(a_dumps)
print('--------dumps--------')
print(a_loads)  # {'x': 1, 'y': 2, 'z': True}
print(type(a_loads))  # dict

### use dump to create .json file and use load to read .json file
with open('./json_test.json', 'w') as fw:
    json.dump(a, fw)
    print('dict -> .json file successfully')

### 
with open('./json_test.json', 'r') as fr:
    load_f = json.load(fr)
    print(load_f)
    print('load .json file successfully')
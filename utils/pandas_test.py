#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''pandas practice'''

import pdb
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
# s = pd.Series(list('abca'))
# print(s)
# print(pd.get_dummies(s))
# pdb.set_trace()


df = pd.DataFrame(np.arange(16).reshape((4,4)),index=['a','b','c','d'],columns=['one','two','three','four'])
print(df)
print('-----------------')
# print(df.loc[:, 'one':'three'])

### 取列
# print(df.four)  # 等同于:print(df.loc[:,['three', 'four']])  等同于:print(df['four'])
# print(df.loc[:,['three', 'four']])
# print(df.loc[:,'four'])
# print(df['four'])

### 取一个值
# print(df.loc['a','one'])

### 测试独热编码
# add a new column
df['color'] = ['red', 'green', 'yellow', 'blue']
df['cate'] = ['1', '2', '3' ,'4']
print(df)
# df['color'] = LabelEncoder().fit_transform(df['color'])
# print(df)
# # print(type(df_label))
# df['color'] = OneHotEncoder().fit_transform(df['color'].values.reshape(-1,1)).toarray()
# print(df['color'])
# print(df)


print(df.iloc[:, 2].dtype)
# df_dummy = pd.get_dummies(df, columns=['color'])
df_dummy = pd.get_dummies(df)
print(df_dummy)
df_dummy['new'] = 1
print(df_dummy)

# print(df_dummy[0:2])  # 取第一行和第二行
# print(df_dummy[:2])  # 取第一行和第二行
# print(df_dummy.iloc[:,0:2])

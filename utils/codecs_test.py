#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs

'''
python对多国语言的处理是支持的很好的，它可以处理现在任意编码的字符，这里深入的研究一下python对多种不同语言的处理。
有一点需要清楚的是，当python要做编码转换的时候，会借助于内部的编码，转换过程是这样的：
原有编码 -> 内部编码 -> 目的编码 

'''

def checkSystem():
    print('python的内部是使用unicode来处理的，但是unicode的使用需要考虑的是它的编码格式有两种，一是UCS-2，它一共有65536个码 位，另一种是UCS-4，它有2147483648g个码位')
    print('本系统使用：{}'.format(sys.maxunicode))
    print('UCS-4' if sys.maxunicode==1114111 else 'UCS-2')


def transformCode():
    print('original:')
    s = '中文'
    print(type(s))
    print('\n')

    print('encode gb2312')
    s_uni = s.encode('gb2312')
    print(type(s_uni))
    print(s_uni)



if __name__ == '__main__':
    # checkSystem()
    transformCode()


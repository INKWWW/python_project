#!/usr/bin/env python
# -*- coding: utf-8 -*-

import linecache

'''
在python中，有个好用的模块linecache，该模块允许从任何文件里得到任何的行，
并且使用缓存进行优化，常见的情况是从单个文件读取多行。
''' 

def test_read_full():
    '''read all lines in a file'''
    filepath = '../wordCount/test.txt'
    full_content = linecache.getlines(filepath)
    print('full_content： ', full_content)

def test_read_lines():
    '''read particular lines from a file'''
    filepath = '../wordCount/test.txt'
    line1 = linecache.getline(filepath, 0)  # no line numbered zero
    line2 = linecache.getline(filepath, 1)
    line3 = linecache.getline(filepath, 2)
    print('line1: {}'.format(line1))
    print('line2: {}'.format(line2))
    print('line3: {}'.format(line3))


if __name__ == '__main__':
    test_read_full()
    test_read_lines()



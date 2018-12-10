#!/usr/bin/env python
# -*- coding: utf-8 -*-

import linecache

'''
在python中，有个好用的模块linecache，该模块允许从任何文件里得到任何的行，
并且使用缓存进行优化，常见的情况是从单个文件读取多行。

注意：
1）、读取文件之后，不需要使用文件的缓存时，需要在最后清理一下缓存，使linecache.clearcache()清理缓存，释放缓存。
2）、此模块使用内存来缓存文件内容，所以需要耗费内存，打开文件的大小和打开速度和你的内存大小有关系。
''' 

def test_read_full(filepath):
    '''read all lines in a file'''
    full_content = linecache.getlines(filepath)
    print('full_content： ', full_content)


def test_read_lines(filepath):
    '''read particular lines from a file'''
    line1 = linecache.getline(filepath, 0)  # no line numbered zero
    line2 = linecache.getline(filepath, 1)
    line3 = linecache.getline(filepath, 2)
    print('line1: {}'.format(line1))
    print('line2: {}'.format(line2))
    print('line3: {}'.format(line3))


if __name__ == '__main__':
    filepath = '../wordCount/test.txt'
    # print('check the validity of cache: ', linecache.checkcache(filepath))
    test_read_full(filepath)
    test_read_lines(filepath)

    # free cache
    linecache.clearcache()
    print('free cache')

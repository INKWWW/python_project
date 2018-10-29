#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''get the size of a file'''

import os

def get_file_size(file_path):
    size = os.path.getsize(file_path)
    print('Size of this file is {} byte'.format(size))


if __name__ == '__main__':
    file_path = 'C:/Users/Bairong/Desktop/graph.txt'
    get_file_size(file_path)

    file_path2 = 'C:/Users/Bairong/Desktop/11.txt'
    get_file_size(file_path2)

    png_path = 'C:/Users/Bairong/Desktop/error.png'
    get_file_size(png_path)


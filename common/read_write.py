#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd

def write_txt(write_to_file):
    # append mode
    with open(write_to_file, 'a') as f:
        content = ['a\n', 'b\n', 'c\n', 'd\n', 'e\n']
        content2 = ['1\n', '2\n', '3\n']
        f.writelines(content2)  # writelines recieve list of strings as parameter and write them one by one
        for item in content:
            f.write(item)

if __name__ == '__main__':
    write_to_file = './write_test.txt'
    write_txt(write_to_file)
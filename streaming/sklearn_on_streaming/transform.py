#!/usr/bin/env python
# -*- coding: utf-8 -*-

def transform_file(filepath):
    with open(filepath, 'r') as f:
        fr = f.read()
        lines = fr.split('\n')
        with open('iris_test.txt', 'w') as fw:
            for line in lines:
                line_list = line.split(',')
                line_list.pop(-1)
                new_line = ','.join(line_list)
                new_line = new_line + '\n'
                fw.write(new_line)


if __name__ == '__main__':
    filepath = './iris.data.txt'
    transform_file(filepath)




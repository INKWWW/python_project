#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pandas as pd

######## txt to csv ########
def txt2csv(inputpath, outputpath):
    """
    将iris数据转换成csv，并且编号类别为 
    Iris-setosa = 1
    Iris-versicolor = 2
    Iris-virginica = 3
    """
    with open(inputpath, 'r') as f:
        fr = f.read()
        # print(fr)
        # print(type(fr))
        lines = fr.split('\n')
        # print(lines)
        new_lines = [line.split(',') for line in lines]
        # print(new_lines)
        for line in new_lines:
            if 'Iris-setosa' in line:
                line[4] = 1
            elif 'Iris-versicolor' in line:
                line[4] = 2
            else:
                line[4] = 3
        # print(new_lines)
        final_lines = []
        for line in new_lines:
            line = list(map(lambda x:float(x), line))
            final_lines.append(line)
        # print(final_lines)

        with open(outputpath, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in final_lines:
                csv_writer.writerow(line)



######## txt to csv - 无转换，直接读写 ########
def txt2csv_direct(inputpath, outputpath):
    """
    将iris数据转换成csv
    """
    with open(inputpath, 'r') as f:
        fr = f.read()
        lines = fr.split('\n')
        new_lines = [line.split(',') for line in lines]

        with open(outputpath, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in new_lines:
                csv_writer.writerow(line)



######## csv to txt ########
def create_txt_2(inputfile, output_file):
    '''生成的txt文件含所有情况，含有四列的，拿来计算指标'''
    with open(inputfile, 'r') as f:
        reader = csv.reader(f)
        with open(output_file, 'w') as fw:
            for row in reader:
                if reader.line_num == 1:
                    continue
                if row[1] == 'null':
                    row[1] = ' '
                new_row = ','.join([row[0], row[1]]) + '\n'
                fw.write(new_row)




if __name__ == '__main__':
    # inputpath = 'C:\\spark\\data\\my_data\\iris_data.txt'
    # outputpath = 'C:\\spark\\data\\my_data\\iris_data.csv'
    # txt2csv(inputpath, outputpath)


    inputpath = 'C:\\spark\\data\\my_data\\iris_data.txt'
    outputpath = 'C:\\spark\\data\\my_data\\iris_data_ori.csv'
    # txt2csv_direct(inputpath, outputpath)

    for i in range(12):
        print(i)
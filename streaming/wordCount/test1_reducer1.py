#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from itertools import groupby
from operator import itemgetter

def read_from_mapper(file, separator):
    for line in file:
        return line.strip().split(separator, 2)


def main(separator='\t'):
    data = read_from_mapper(sys.stdin, separator)
    print(data)
    for current_word, group in groupby(data, itemgetter(0)):
        print(current_word, group)
        try:
            total_count = sum(int(count) for current_word, count in group)
            # print(current_word, total_count)
            print('{}{}{}'.format(current_word, separator, total_count))
        except ValueError:
            pass

def new_main(separator='\t'):
    current_word = None
    current_count = 0
    word, count = read_from_mapper(sys.stdin, separator)
    count = int(count)
    if word == current_word:
        current_count += count
    else:
        if current_word:
            print('{}{}{}'.format(current_word, separator, total_count))
        current_word = word
        current_count = count



if __name__ == '__main__':
    main()


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def read_from_input(file):
     # with open(file, 'r', encoding='utf-8') as f:
     #    fr = f.read()
     #    words = fr.split()
     #    words = [word.strip() for word in words]
     #    for word in words:
     #        yield word
     for line in file:
        yield line.split(' ')


def main(separator = ' '):
    data = read_from_input(sys.stdin)
    for words in data:
        for word in words:
            # write to reducer
            print('{}\t{}'.format(word, 1))

if __name__ == '__main__':
    main()

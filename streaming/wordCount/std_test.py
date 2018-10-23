#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def stdin_test(file):
    with open(file, 'r', encoding='utf-8') as f:
        fr = f.read()
        words = fr.split()
        words = [word.strip() for word in words]
        # print(words)
        for word in words:
            yield word


def test1():
    word = 'word1' + '\t' + '1'
    print(word)
    print('{}\t{}'.format('word2', 1))
    new = word.split('\t')
    print(new)


if __name__ == '__main__':
    # stdin_test('./test.txt')
    test1()
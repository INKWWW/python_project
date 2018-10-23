#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    for line in sys.stdin:
        words = line.split()
        for word in words:
            # print('{}\t{}'.format(word, 1))
            print('%s%s%d' % (word, '\t', 1))

if __name__ == '__main__':
    main()
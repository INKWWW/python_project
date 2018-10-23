#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cat xxxx.txt | ./map.py | sort | ./reduce.py  -> 直接本机查看是否能够运行
# cat test.txt | ./mapper1.py | sort | ./reducer1.py


##### 注意reducer接收的输入是排好序的！ #####

import sys

def main():
    curr_word = None
    curr_count = 0
    for line in sys.stdin:
        word, count = line.split('\t')
        count = int (count)
        if word == curr_word:
            curr_count += count
        else:
            if curr_word:
                # print('{}\t{}'.format(curr_word, curr_count))
                print('%s%s%d' % (curr_word, '\t', curr_count))
            curr_word = word
            curr_count = count
    if curr_word == word:
        # print('{}\t{}'.format(curr_word, curr_count))
        print('%s%s%d' % (curr_word, '\t', curr_count))

if __name__ == '__main__':
    main()
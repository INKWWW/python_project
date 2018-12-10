#!/usr/bin/env python
# -*- coding: utf-8 -*-

def star_traverse_set():
    test_set = ((1, 2), (2, 3), (3, 4), (4, 5))
    for item in test_set:
        print('*item_set: {}'.format(*item))


def star_traverse_list():
    test_list = [(1, 2), (2, 3), (3, 4), (4, 5)]
    # for item in test_list:
    print('*item_list: {}'.format(*test_list))



if __name__ == '__main__':
    print('### test star set ###')
    star_traverse_set()
    print('### test star list ###')
    star_traverse_list()




#!/usr/bin/env python
# -*- coding: utf-8 -*-

def dictDel():
    dd = {'name': 'bob', 'age':23, 'sex': 'male'}
    print('dict dd is: ', dd)
    del dd['age']
    print('after deleting age:', dd)
    dd.clear()
    print('clear this dict: ', dd)
    del dd 
    # print('delete this dict: ', dd) #
    print('delete this dict')

if __name__ == '__main__':
    dictDel()




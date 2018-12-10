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


class A(object): 
    def __init__(self): 
        self['B'] = "BB" 
        self['D'] = "DD" 
        del self['D'] 
        # print('__init__: {}'.format(self.__init__))
       
    def __setitem__(self,name,value): 
        '''''
        @summary: 每当属性被赋值的时候都会调用该方法，因此不能再该方法内赋值 self.name = value 会死循环
        ''' 
        print("__setitem__:Set {} Value {}".format(name,value))
        self.__dict__[name] = value 
       
    def __getitem__(self,name): 
        ''''' 
        @summary: 当访问不存在的属性时会调用该方法
        ''' 
        print("__getitem__:No attribute named '{}'".format(name))
        return None 
       
    def __delitem__(self,name): 
        ''''' 
        @summary: 当删除属性时调用该方法
        ''' 
        print("__delitem__:Delete attribute '{}'".format(name))
        del self.__dict__[name] 
        print(self.__dict__) 


if __name__ == '__main__':
    # dictDel()

    print('### __init__ process: ###')
    X = A() 
    print('### check bb in this dict ? ###')
    b = X['bb'] 
    print('### add key:value to this dict: ')
    X['cc'] = 'CC'




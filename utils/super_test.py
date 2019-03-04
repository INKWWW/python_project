#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''测试子类继承父类中的super'''

class Father(object):
    """docstring for Father"""
    def __init__(self, name):
        self.name = name
        print(name)
        return

    def callMeFather(self):
        print('### In Father\'s Class ###')
        print('I am your {} from Father\'s initial param'.format(self.name))
        print('I am your Father')
        return


class Child(Father):
    """docstring for Child"""
    def __init__(self, name):
        super().__init__(name)
        # self.name = 'GrandMMMMMother'
        # self.name = name
        print('I am ur {}'.format(name))
        return

    def callMeBaby(self):
        print('You are my baby')
        # super(Child, self).callMeFather()  # python2写法
        super().callMeFather()  # python3写法


if __name__ == '__main__':
    print('=======Father init======')
    fatherInstance = Father('Father\'s Father')
    print('=======call Father\'s Class=======')
    fatherInstance.callMeFather()

    print('=======Child init=======')
    childInstance = Child('GrandFFFFFather')
    print('=======call Child\'s Class=======')
    childInstance.callMeBaby()



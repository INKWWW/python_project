#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ClassTest(object):
    """docstring for ClassTest"""
    # hobby = 'basketball'
    # hobby1 = []  # for getHobby_2
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        # self.hobby = hobby

    @classmethod
    def getHobby_1(cls, hobby, name):  # hobby参数需要在调用的时候传入
        # hobby = 'basketball'
        hobby.append('basketball')
        hobby.append('football')
        print(hobby)
        print('#####: {}'.format(name))
        # print('@@@@@: {}'.format(self.age))  # error - NameError: name 'self' is not defined
        # print(cls.hobby)
        # return cls.hobby

    @classmethod
    def getHobby_2(cls):  # hobby参数在class里面已经定义了，并且需要cls来取这个参数
        # hobby = 'basketball'
        # cls.hobby1.append('basketball')
        # cls.hobby1.append('football')
        cls.hobby1 = '11111'
        print(cls.hobby1)
        # print('$$$$')
        # print(self.name)  # 不行的 error
        # print(cls.hobby)
        # return cls.hobby

    @classmethod
    def addNewVar(cls):
        cls.newItem = 'new one'  # 新加入一个变量


    # @classmethod
    def getInfo(self, new):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.newItem)
        print('****: {}'.format(new))
        print('^^^^: {}'.format(self.hobby1))


if __name__ == '__main__':
    classTest = ClassTest('W', 20, 'male')
    #########################
    # hobby = []
    # ClassTest.getHobby_1(hobby, classTest.name)
    #########################
    ClassTest.getHobby_2()
    #########################
    # 添加新的变量
    ClassTest.addNewVar()

    # 打印值
    classTest.getInfo('new')
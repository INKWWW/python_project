# 容器

'''容器是用来储存元素的一种数据结构，容器将所有数据保存在内存中，Python中典型的容器有：list，set，dict，str等等。

for … in… 这个语句其实做了两件事。第一件事是获得一个可迭代器，即调用了__iter__()函数。 
第二件事是循环的过程，循环调用__next__()函数。

对于test这个类来说，它定义了__iter__和__next__函数，所以是一个可迭代的类，也可以说是一个可迭代的对象（Python中一切皆对象）。
'''
print('------容器------')
class test(object):
    """docstring for test"""
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data

for item in test(3):
    print(item)

# 迭代器

'''含有__next__()函数的对象都是一个迭代器，所以test也可以说是一个迭代器。如果去掉__itet__()函数，test这个类也不会报错。
'''
print('------迭代器------')
class test(object):
    """docstring for test"""
    def __init__(self, data):
        self.data = data

    def __next__(self):
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data

t = test(3)
for i in range(3):
    print(t.__next__())


# 生成器

'''生成器是一种特殊的迭代器。当调用fib()函数时，生成器实例化并返回，这时并不会执行任何代码，生成器处于空闲状态，注意这里prev, curr = 0, 1并未执行。然后这个生成器被包含在list()中，list会根据传进来的参数生成一个列表，所以它对fib()对象(一切皆对象，函数也是对象)调用__next()__方法，
'''
print('------生成器------')
def fib(end = 1000):
    prev, curr=0,1
    while curr < end:
        yield curr
        prev, curr = curr, curr + prev


print(list(fib()))





#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy  as np

def test_endpoint():
    array_1 = np.linspace(1, 10, 10)
    print('array_1 with default endpoint: True : {}'.format(array_1))

    array_2 = np.linspace(1, 10, 10, endpoint=False)
    print('try1--array_2 with endpoint=False: {}'.format(array_2))

    array_2 = np.linspace(1, 10, 10, endpoint=False, retstep=True)
    print('try2--array_2 with endpoint=False and retstep=True: {}'.format(array_2))


if __name__ == '__main__':
    test_endpoint()


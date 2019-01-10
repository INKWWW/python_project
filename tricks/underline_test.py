#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def testOsWalk(filepath):
    for _, _, filename in os.walk(filepath):
        print('filename: {}'.format(filename))



if __name__ == '__main__':
    filepath = '../test_files'
    testOsWalk(filepath)

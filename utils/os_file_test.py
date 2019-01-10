#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def testOsWalk(filepath):
    for dirpath, dirname, filename in os.walk(filepath):
        print('dirpath: {}'.format(dirpath))
        print('dirname: {}'.format(dirname))
        print('filename: {}'.format(filename))


def testOsPathSplitext(filepath):
    for _, _, filename in os.walk(filepath):
        print('filename: {}'.format(filename))
    for file in filename:
        if os.path.splitext(file) == '.hdf5':
            print('That is it')



if __name__ == '__main__':
    filepath = '../test_files'
    print('### test os.walk ###')
    testOsWalk(filepath)
    print('### test os.path.splitext ###')
    testOsPathSplitext(filepath)
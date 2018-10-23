#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


# print(__file__)

scriptPath = os.path.realpath(__file__)
print('scriptPath: ', scriptPath)

dirname, filename = os.path.split(__file__)
print('dirname: ', dirname)
print('filename: ', filename)

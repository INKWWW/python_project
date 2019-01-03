#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

def timeGap(date1, date2):
    time1 = datetime.datetime(int(date1[0:4]), int(date1[4:6]), int(date1[6:8]))
    time2 = datetime.datetime(int(date2[0:4]), int(date2[4:6]), int(date2[6:8]))
    print('time1 is ', time1)
    print('time2 is ', time2)
    gap = (time1 - time2).days
    print('gap is ', gap)
    return gap



if __name__ == '__main__':
    date1 = '20181008152339'
    date2 = '20181001104600'
    timeGap(date1, date2)

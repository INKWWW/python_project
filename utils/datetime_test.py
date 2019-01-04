#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime 
from datetime import timedelta
import time

def timeGap(date1, date2):
    '''calculate the gap between two time'''
    time1 = datetime(int(date1[0:4]), int(date1[4:6]), int(date1[6:8]), int(date1[8:10]))
    time2 = datetime(int(date2[0:4]), int(date2[4:6]), int(date2[6:8]))
    print('time1 is ', time1)
    print('time2 is ', time2)
    gap = (time1 - time2).days
    print('gap is ', gap)
    return gap


def tomorrow():
    '''get the detailed date of tomorrow'''
    now = datetime.now()
    print("now: ", now)
    aDay = timedelta(days=1)  # -1: yesterday
    now = now + aDay
    print("tomorrow: ", now.strftime('%Y-%m-%d'))


def nextYear():
    now = datetime.now()
    next_year = now + timedelta(days=365)
    print('next year is', next_year)


def lastMonth():
    '''find last month'''
    now_struct_time = time.localtime()
    print('now_struct_time: ', now_struct_time)
    last_month = now_struct_time[1] - 1 or 12
    print('last month is ', last_month)


if __name__ == '__main__':
    date1 = '20181008152339'
    date2 = '20181001104600'
    timeGap(date1, date2)

    #####
    # tomorrow()

    #####
    # nextYear()

    #####
    # lastMonth()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
目标：对某一函数设置执行时间，如果超时，则进行相应处理
方法：将可能超时的函数使用另一线程执行，如果超时，则主线程放弃等待，进行相应的处理

'''

import time
import threading

# 可以修改成任意需要执行的函数
def deriveDataFromDB():
    print('operating... 开始执行子线程-deriveDataFromDB函数')
    time.sleep(5)  # 推迟5秒执行（假设是该函数进行的操作）
    print('子线程成功执行')
 

if __name__ == '__main__':
    print('当前我们在主线程中\n')

    print('deriveDataFromDB放入子线程中执行\n')
    sub_thread = threading.Thread(target=deriveDataFromDB)  # 创建子线程

    print('设置子线程并开启子线程\n')
    sub_thread.setDaemon(True)  # 设置子线程在在主线程结束时直接被kill
    sub_thread.start()

    print('让主线程等待子线程3秒... \n')
    sub_thread.join(3)  # 修改此处参数，大于5则可以成功执行子线程
    # sub_thread.join(6)

    print('主线程执行结束')
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/17 20:28
# @File    : 12time.py
# @Function:

import time
import os
import sys
# print(time.time()) # 从格林威治时间到现在的时间，1970到现在的秒数
#
# print(time.localtime())  #返回包含当前所有时间的元祖

# print(time.asctime())

# print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 返回一个格式化  当前时间戳的函数 获取当前的函数

together_time = '2018-9-2 00:00:00'
x = time.strptime(together_time, '%Y-%m-%d %H:%M:%S')  # 返回时间的元祖
# print(time.strftime('%Y-%m-%d %H:%M:%S',x))
# a = time.mktime(x) # 将时间的元祖 转换成秒数
# b = time.time() - a

a = time.time() - time.mktime(x)
b = a / 60
c = b / 60
d = c / 24
e = d/ 365

while True:
    #print('现在是和飞飞在一起的%.2f 秒'% a)
    # print('现在是和飞飞在一起的%.2f 分'% b )  # 在一起的分数
    # print('现在是和飞飞在一起的%.2f 时'% c)  # 在一起的小时数
    # print('现在是和飞飞在一起的%.2f 天'% d)  # 在一起的天
    # print('现在是和飞飞在一起的%.2f 年'% e)  # 在一起的年
    #print(time.time())
    print("\r", '现在是和飞飞在一起的%.2f 秒'% (time.time() - time.mktime(x)), end='', flush=True)
    #print("\r", '现在是和飞飞在一起的%.2f 分' % (time.time() - time.mktime(x)/60), end='', flush=False)
    time.sleep(0.4)







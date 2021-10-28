#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 11:00
# @File    : 6.py
# @Function:

def func():
    for i in range(100):
        print(i)
        yield i  # 使用yield方法，这样子不会一次性执行，需要时调用，减少内存的占用


myfunc = func()
next(myfunc)  # next 配合yield使用，next一次，执行一次
next(myfunc)

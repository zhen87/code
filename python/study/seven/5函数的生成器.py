#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 10:53
# @File    : 5函数的生成器.py
# @Function:

def demo():
    print('123')
    yield 10
    print('123')
    print('123')
a = demo()
print(next(a))
next(a)
next(a)
next(a)
next(a)

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/17 19:39
# @File    : 装饰器.py
# @Function:

def demo(x):
    print('oooooooooooo')
    x()

def func():
    print('xxxxxxxxxxxxxxxxxx')

#在其他语言里 称为回调函数  也就是传进去的参数 是一个函数名
demo(func)





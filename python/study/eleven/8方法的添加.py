#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/8 19:12
# @File    : 8方法的添加.py
# @Function:

from types import MethodType
class Demo:
    pass
demo =Demo()
def run(self):
    print('我是一个新添加的方法')
demo.run = MethodType(run,demo) # 只能给我当前的对象添加该方法
demo.run()
demo2 =demo()
demo2.run()
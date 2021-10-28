#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/9 10:47
# @File    : 9类的方法的添加.py
# @Function:

class Test:
    pass

def run(self,x):
    print('我是后加的类的方法', x)

Test.run = run

t = Test()
t.run('w')
print(Test.__dict__)
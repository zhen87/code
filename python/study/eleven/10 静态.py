#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/9 10:58
# @File    : 10 静态.py
# @Function:

class Demo:
    name = 'xx'
    @staticmethod
    def run():
        print('run')
    def __str__(self):
        print('我是输出当前对象时会调用的方法')
    def __del__(self):
        print('是不是我')
# Demo.run()  #run

d = Demo()
d.run()  #run,是不是我
d.age =18
print(d.age)

del d
while True:
    print('1')
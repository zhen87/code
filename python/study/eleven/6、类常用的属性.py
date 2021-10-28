#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/8 18:55
# @File    : 6、类常用的属性.py
# @Function: 类常用的属性

class A:
    pass


class Demo(A):
    """
    我是一个demo的类
    """
    name = '张三'

    def speak(self):
        print('说的方法')


d = Demo()
print(Demo.__doc__)  # 获取类的说明   我是一个demo的类
print(Demo.__name__) # 返回类名   我是一个demo的类
print(Demo.__base__) # <class '__main__.A'>
print(Demo.__dict__) # 返回类的所有的信息  {'__module__': '__main__', '__doc__': '\n
#  我是一个demo的类\n   # ', 'name': '张三', 'speak': <function Demo.speak at 0x03A312B8>}

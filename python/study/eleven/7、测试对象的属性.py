#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/8 19:04
# @File    : 7、测试对象的属性.py
# @Function:

class Test:
    __slots__ = ('name','sex','hobby','age') # 限制属性的动态添加，只允许添加在我的元祖里面的属性名
t = Test

# print(hasattr(t,'namew')) # 判断是否有某个属性存在
# print(getattr(t,'sexx',404))
# print(getattr(t,'x','y'))
# print(t.x)

t.name ='张三'
t.a = 'a'
t.b = 'b'
t.c = 'c'


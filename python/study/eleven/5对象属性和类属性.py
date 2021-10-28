#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/7 19:04
# @File    : 5对象属性和类属性.py
# @Function:

class Person:
    name = '我是一个Persion'
p = Person()
print(p.name)
print(Person.name)
p.name = 'xxx'
p.age = 18
print('---------------------')
print(p.name)
print(Person.name)
print(p.age)
print(Person.age)

# newP = Person()
# print(newP.name)
# print(newP.age)
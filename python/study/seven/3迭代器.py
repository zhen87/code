#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 10:24
# @File    : 3.py
# @Function:迭代器

from collections import Iterable
print(isinstance((), Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('', Iterable))
print(isinstance(1,Iterable))


str1 = '1bcdf'
mylist = iter(str1)
for x in mylist:
    print(x)

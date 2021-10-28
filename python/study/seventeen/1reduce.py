#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/13 17:30
# @File    : 1reduce.py
# @Function:

from functools import reduce
mylist = [1,2,3,4,5,6]

def mysum(x,y):
    return x+y

l = reduce(mysum,mylist)
print(l)


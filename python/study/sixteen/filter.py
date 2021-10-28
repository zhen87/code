#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/13 16:24
# @File    : filter.py
# @Function:

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 将奇数过滤，留下的返回True，不要的返回False
def demo(num):
    if num % 2 == 0:
        return True
    return False

newlist = filter(demo, mylist)
print(list(newlist))

# for i in mylist:
#     print(i,demo(i))


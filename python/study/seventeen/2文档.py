#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/13 17:50
# @File    : 2文档.py
# @Function:

import doctest
def mySum(x,y):
    '''
    这是一个求和的函数
    :param x:
    :param y:
    :return:
    >>> print(mySum(1,4))
    2
    '''
    return x+y

print(mySum(1,2))

# 文档测试
doctest.testmod()



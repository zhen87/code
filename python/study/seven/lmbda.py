#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/20 16:51
# @File    : lmbda.py
# @Function:匿名函数


# 文件出现2个或者多个相同的名字的函数，那么上面的会被下面同名的函数覆盖掉
# 函数名区分大小写
def sp():
    print('1')

def sp():
    print('2')


# sp()
# 匿名函数
mymangod = lambda a, b: a + b
print(mymangod(1, 2))


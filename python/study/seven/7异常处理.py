#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 11:09
# @File    : 7异常处理.py
# @Function:

try:
    pass  # 可以出现错误异常的代码
except TypeError as t:  # 给错误类型起一个别名
    print(t)  # 将错误输出
except ValueError as v:  # 进行多层捕获
    print(v)  # 将错误输出
except:
    pass  # 出现了异常，但是没有符合我错误异常的错误类型，走最后的except


try:
    pass  # 可以出现错误异常的代码
except TypeError as t:  # 给错误类型起一个别名
    print(t)  # 将错误输出
else:
    pass  # 代码没有出现任何错误的情况下，走else逻辑

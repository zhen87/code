#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/15 20:53
# @File    : 9.py
# @Function: *args && **args

# def func(*args):#不确定的形参数,元祖展示
#     #print(args)
#     for i  in args:
#         print(i)
# func(1, 2, 3, 4)


def func(**args):#不确定的形参数,字典展示
    for i in args:
        print(i,args[i])

func(A='a',B='b')

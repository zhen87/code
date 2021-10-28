#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/12 11:29
# @File    : 13 高阶函数.py
# @Function:

# 简单的函数
mylist = [2,6,-8,7,-1]
mylist2 = sorted(mylist) # 默认是升序
mylist2 = sorted(mylist,key=abs)  # 按照绝对值来排序
mylist3 = sorted(mylist,reverse=True)  # 倒序
print(mylist3)

mylist = ['abcgs','abc','sdfghjkrth','45678ghjkl']

def mylen(str):
    return len(str)
mylist4 = sorted(mylist,key=mylen)
print(mylist4)
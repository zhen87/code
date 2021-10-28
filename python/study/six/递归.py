#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/20 15:46
# @File    : 递归.py
# @Function: 递归

# def newadd(x):
#     if x == 0:
#         return 0
#     return x + newadd(x - 1)
#
#
# print(newadd(3))

def demo(x):
    print(x)
    if x>0 :
        demo(x-1)
    print('-',x)
demo(3)

def a(x): #2
    print(x)#2
    b(x-1)
    print('a',x)#2
def b(x):#1
    print(x)#1
    c(x-1)
    print('b',x)# 1
def c(x):#0
    print(x)#0
    print('c',x) # 0


a(2)
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/15 20:36
# @File    : 8.py
# @Function: 函数关键字 globle、nonlocal

username = '我是函数外部的变量'
def func1():
    username = '快不快'

    def func2():
        global username
        print('2', username)
        username = 'B '
        print('3', username)

    func2()
    print('4', username)


print('1', username)

func1()

print('5',username)

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/1 15:35
# @File    : 2、私有方法.py
# @Function:

class Money:
    __money = 1000
    name = 'father'
    def __getMoney(self):
        print('money为',self.__money)
    def getMoney(self):
        self.__getMoney()
        print('我是公有方法去调用的私有方法__getMoney()')

m = Money()
m.getMoney()
# m.__getMoney()
print(m._Money__money)
print(m._Money__getMoney())# 在外部私有方法的调用

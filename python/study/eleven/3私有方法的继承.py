#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/1 18:23
# @File    : 3私有方法的继承.py
# @Function:

class Money:
    __money = 1000
    name = 'father'
    def __getMoney(self):
        print('money为',self.__money)
    def run(self):
        print('我在父类里面')
class sonMoney(Money):
    def get(self):
        print(self.name)
        # print(self.__money)#没有被继承
        self.run()#可以调用
        self.__getMoney() #报错
son = sonMoney()
# #print(son._Money__monney)
# print(sonMoney.__Money__money)
# son.get()
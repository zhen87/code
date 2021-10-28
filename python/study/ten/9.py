#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/31 16:42
# @File    : 9.py
# @Function:

class Year:

    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, year):
        self.__birth = year

    def age(self,now): #传入当前年份的参数
        return now - self.birth  #用传进去的年减去 你的出生年  获取到的年龄值

year = Year()
# year.set_birth(1988)
# print(year.get_birth())
year.birth = 1988
print(year.age(2017))


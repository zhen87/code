#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/27 19:52
# @File    : 8.py
# @Function:

class Demo:
    @property  #获取值
    def age(self):
        return self._age
    @age.setter  #setter属性为我们的私有属性设置值，代表修改
    def age(self, age): #这个方法给什么赋值都正常，但一定要将他的名字和当前设置私有属性的名字统一，不然会被误解为其他的属性
        if not isinstance(age, int):
            raise TypeError('你输入的数据类型不对')
        if age < 1 or age > 99:
            raise ValueError('数值超出正常年龄的范围')
        self._age = age

demo =Demo()
# demo.set_age(88)
# print(demo.get_age())
demo.age=10
print(demo.age)



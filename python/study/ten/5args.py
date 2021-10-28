#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/20 15:25
# @File    : 5args.py
# @Function:

class Demo:
    def test(self, name, age, sex, hobby):
        self.name = name
        self.age = age
        self.sex = sex
        self.hobby = hobby


demo1 = Demo()
demo1.test('张三', 18, 'man', 'sing')
print(demo1.name)
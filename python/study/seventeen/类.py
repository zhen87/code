#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 17:26
# @File    : 类.py
# @Function:

class Demo:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def get_age(self):
        return self.age
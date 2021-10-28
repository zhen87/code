#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/4 16:43
# @File    : 4、多继承.py
# @Function:

class Dog:
    def __init__(self):
        print('我是被 吕洞宾冤枉的')
    def erLangShen(self):
        print('我的兄弟是 哮天犬')
    def run(self):
        print('Dog run')
class Bird:
    def __init__(self):
        print('我要飞的更高')
    def wangfeng(self):
        print('我会唱鸟语的哥')
    def run(self):
        print('鸟 飞')
class Son(Bird,Dog):
    def run(self):
        Dog.run(self)
s = Son()
s.run()
# s.erLangShen()
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/17 19:56
# @File    : 11、.py
# @Function: 装饰器

# import os
#
# os.rename('11、.py','11.py')

# def demo(x):
#     def inner():
#         print('ooooooooooooo')
#         x()
#     return inner()
#
# # def func():
# #     print('xxxxxxxxxxxx')
#
#
# func= demo(func())
# func()


def demo(x):
    def inner(age):
        if age <= 10:
            mystr = 'childer'
        elif age <= 20:
            mystr = 'teenager'
        else:
            mystr = 'older'
        # print(mystr)
        x(mystr)
    return inner
@demo   #  @demo 相当于func = demo（func）
def func(person):
    print('是一个', person)

func = demo(func)
func(30)




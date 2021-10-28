#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 10:03
# @File    : 列表推导式.py
# @Function:


# 列表推导式 提供快速创建列表的方法

mylist = [x for x in range(100)]
mylist1 = [(x, x+10) for x in range(100)] # 列表里嵌套元祖
mylist2 = [[x, x+10] for x in range(100)] # 创建二维数组，第一个是本身，第二个值是本身+10
mylist3 = [x for x in range(100) if x>20 and x< 80] #添加过滤的作用
mylist4 = [[x,y]  for x in range(10)  for y in range(5)]  #for循环的嵌套
print(mylist)
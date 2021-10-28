#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/13 18:13
# @File    : 3 单元测试.py
# @Function:
import unittest
from hanshu import mysum
from hanshu import mysub

# class Test(unittest.TestCase):
#     def setUp(self):
#         print('开始测试的时候调用的')
#     def tearDown(self):
#         print('测试结束调用')
#     # 测试相加的方法
#     def test_mysum(self):
#         self.assertEqual(mysum(1,2),3,'加分错误')
#     def test_mysub(self):
#         self.assertEqual(mysub(2,1),2,"减法有误")

class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试的时候调用的")

    def tearDown(self):
        print("测试结束调用我")

    #测试相加的方法
    def test_mySum(self):
        self.assertEqual(mysum(1,2),4,"加法有误")

    def test_mySub(self):
        self.assertEqual(mysub(2,1),2,"减法有误")


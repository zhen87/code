#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 17:33
# @File    : 6开始类的测试.py
# @Function:

from 类 import Demo
import unittest

class Test(unittest.TestCase):
    def test_init(self):
        d = Demo('张三',20)
        self.assertEqual(d.name,'张三','类有bug')

    def test_get_age(self):
        d = Demo('张三',20)
        self.assertEqual(d.get_age(),20,'age有问题')




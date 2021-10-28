#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/24 20:21
# @File    : 4.py
# @Function:

import re
mystr = 'wertyttttttttaqqq'
# print(re.split(' ',mystr))
# print(re.split('\s',mystr))
# print(re.split('\S',mystr))  # 按照空白字符来拆分
# print(re.findall('t',mystr))
# print(re.finditer('a',mystr))
x = re.finditer('w',mystr)
print(next(x))








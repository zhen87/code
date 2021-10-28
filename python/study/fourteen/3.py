#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/24 19:40
# @File    : 3.py
# @Function:

import re

mystr = '<b>啊啥时候</b><i>实打实</i><b>啊啥时候</b><b>啊啥时候</b><b>123456</b>'

print(re.sub('<b>(.*?)</b>', '<i>\\1</i>', mystr))
print(re.subn('<b>(.*?)</b>', '<i>\\1</i>', mystr))
print(re.subn('<b>(.*?)</b>', '<i>\\1</i>', mystr,1))


# year = '12-10-2017'
# # 替换成正常的年月日  2017-12-10
# # 替换成正常的年月日，分割使用年月日  2017年12月10日
#
# print(re.sub('(\d{2})-(\d{2})-(\d{4})','\\3-\\1-\\2',year))
# print(re.sub('(\d{2})-(\d{2})-(\d{4})','\\3年\\1月\\2日',year))
# print(re.sub('12','21',year))





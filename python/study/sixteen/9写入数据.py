#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 15:50
# @File    : 9写入数据.py
# @Function:

from pyexcel_xls import save_data
from collections import OrderedDict
path = r'C:\Users\admin\Desktop\test1\3.xls'
data = {'表一':[[1,2,3],[1,2,3]],'表二':[[1,2,3],[1,2,3]]}
dic = OrderedDict()
# 返回可遍历的字典，返回一个键值对
for name,value in data.items():
    d = {}
    d[name] = value
    dic.update(d)
save_data(path,dic)
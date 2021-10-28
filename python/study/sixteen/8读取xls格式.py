#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 15:18
# @File    : 8读取xls格式.py
# @Function:

from collections import OrderedDict # 有序字典类型
from pyexcel_xls import get_data

path = '1.xls'
def read_xls(path): # 读取xls 和xlsx
    dic = OrderedDict()
    data = get_data(path)
    for sheet in data:
        dic[sheet] = data[sheet]
        return dic
print(read_xls(path))


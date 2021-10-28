#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/11 16:29
# @File    : dict.py
# @Function:
import pickle
# 对mysql文件进行初始化
#path = 'mysql.txt'
path = 'mysql_3.txt'
# dict = {}
# with open(path, 'wb') as f:
#     pickle.dump(dict, f)

with open(path,'rb') as f1:
    print(pickle.load(f1))


# 62979
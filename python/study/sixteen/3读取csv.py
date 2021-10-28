#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 10:50
# @File    : 3读取csv.py
# @Function:

import csv
path = '000001.csv'
def read_csv(path):
    mylist = []
    with open(path,'r') as f:
        info = csv.reader(f)
        for i in info:
           mylist.append(i)
        return mylist
print(read_csv(path))
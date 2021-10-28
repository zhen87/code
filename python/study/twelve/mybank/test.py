#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/21 16:28
# @File    : test.py
# @Function:
import pickle

path = 'mysql_3.txt'
cardLock_new = 'True'
cardLock_old = 'False'
file_date = []
with open(path, 'rb') as f:
    for line in f.readlines():
        line = line.replace(str.encode(cardLock_new), str.encode(cardLock_old))
        # line = line.replace(cardLock_new,cardLock_old)
        file_date.append(line)
        print(file_date)

with open('1.txt', 'wb') as f1:
    pickle.dump(file_date, f1)
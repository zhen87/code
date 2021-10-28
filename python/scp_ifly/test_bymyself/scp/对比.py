#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/2 15:33
# @File    : 对比.py
# @Function:

import codecs
f = codecs.open('sun.txt','rb', encoding='utf-8',errors='ignore')
f1 = f.read()
m = codecs.open('sun1.txt','rb', encoding='utf-8',errors='ignore')
m1 = m.read()
# print(len(m1))
# print(len(f1))
f2 = []
m2 = []
x = 0
for i in range(len(f1)):
    f2 = f1[i].split('/')
    m2 = m1[i].split('/')
    # print(m2)
    if f2 == m2:
        x += 1
        print('true')

    else:
        print('error')
print(x)
print(len(f1))
print(len(m1))

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 16:39
# @File    : lianxi.py
# @Function:

import codecs
# path = r'C:\Users\admin\Desktop\test.txt'
f1 = codecs.open('test1.txt', 'wb', encoding='utf-8', errors='ignore')
f = codecs.open('test.txt', 'rb', encoding='utf-8', errors='ignore')
line = f.readlines()
line1 = []
for i in line:
    #for x in i:
        # if len(x) == 0:
        #     continue
        line1 = ''.join(i).replace('{', '').replace('}', '').replace('"', '').replace(':', '').replace('(', '') \
            .replace('_', '').replace(',', '').replace('[', '').replace(']', '').replace(')', '').replace('$', '') \
            .replace('\n', '').replace(' ', '')
        if len(line1) == 1:
            continue
        # print('这是长度',len(line1))
        # print('这是原文',line1)
        f1.write(line1)
f.close()
f1.close()

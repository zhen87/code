#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 11:29
# @File    : 9匹配qq号.py
# @Function:

import urllib.request
import re

data = urllib.request.urlopen('https://bbs.tianya.cn/m/post-140-393974-6.shtml')
#all_date = data.readline().decode('utf-8')

# prg = re.compile('\w{4,10}',)
# print(prg.findall(all_date))

while True:
    line = data.readline().decode('utf-8')
    if line:
        if line.find('qq') !=-1 or line.find('Qq') != -1 or line.find('QQ') != -1:
            prg = re.compile('[1-9]\d{4,10}',)
            print(prg.findall(line))
    else:
        break
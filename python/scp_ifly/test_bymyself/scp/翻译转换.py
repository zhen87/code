#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/11/23 9:36
# @File    : 翻译转换.py
# @Function:

from copy import deepcopy
import re
def save_file(res_line):
    path1 = r'../txt/2020-11-12广州恒大淘宝-江苏苏宁易购.txt'
    with open(path1,'w') as f1:
        line = ''.join(res_line).replace("'",'').replace(",",'\r\n').replace('"','').replace('[','').replace(']','')
        f1.write(line)
path = r'../txt/subtitle.text.2020-11-12广州恒大淘宝  -  江苏苏宁易购.log'
with open(path,'r',encoding='utf-8') as f:
    line = []
    for word in f.readlines():
        word = word.replace('\n', '')
        if '--' not in word:
            line.append(word)
        print(line)
        res_line = str(deepcopy(line))
        save_file(res_line)
        # line = []





#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/19 17:07
# @File    : ist转写文本规整.py
# @Function:

from copy import deepcopy
def save_file(res_line):
    with open('../txt/ist_test.txt', 'w') as tf:
        line = ''.join(res_line).replace('"',"").replace("*/", '').replace('lab','pcm|').replace('Test','\r\nTest')
        tf.write(line)
with open('../txt/ist.txt', 'r',encoding='utf-8') as tf:
    line = []
    is_start = False
    for word in tf.readlines():
        word = word.replace('\n', '')
        if 'lab' in word:
            is_start = True
        if is_start:
            line.append(word)
        # print(line)
        if 'lab' in word:  # 加一层判断，写入文件更快，
            res_line = deepcopy(line)
            save_file(res_line)






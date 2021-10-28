# -*- coding: utf-8 -*-
# @Author  : pycircus
# @Time    : 2020/3/18 10:26 上午
# @Function:
from copy import deepcopy

def save_file(file_name, res_line):
    with open(file_name, 'w') as tf:
        # line1 = ''.join(res_line)
        line = ''.join(res_line).replace('<s>', '').replace('</s>','')
        # print(line)
        tf.write(line)

with open('../txt/word.txt', 'r') as tf:
    line = []
    is_start = False
    for word in tf.readlines():
        # print(word)
        word = word.replace('\n', '')
        # print(word)
        if 'wav' in word:
            file_name = word.replace('"',"").replace("*/", '').replace('wav', 'txt')
        if '<s>' in word:
            is_start = True

        if is_start:
            line.append(word)

        if '</s>' in word:
            res_line = deepcopy(line)
            save_file(file_name, res_line)
            line = []
            is_start = False



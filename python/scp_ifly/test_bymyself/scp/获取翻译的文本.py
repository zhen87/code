#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/11/23 10:29
# @File    : 获取翻译的文本.py
# @Function:


from copy import deepcopy
import re

path = r'../txt/trans.2020-10-22国安VS鲁能.log'
path1 = r'../txt/国安VS鲁能_获取中文.txt'
def save_file(res_line):
    with open(path1,'w') as f1:
        line = ''.join(res_line).replace("'",'').replace(",",'\r\n').replace('"','').replace('[','').replace(']','').replace('.','').replace('?','').replace('--','').replace('\n', '').replace('-','')
        f1.write(line)
with open(path,'r',encoding='utf-8') as f:
    line = []
    for word in f.readlines():
        word = word.replace('\n', '')
        if '--' not in word:
            # r1 =u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
            word1 = re.sub('[a-zA-Z]','',word)
            line.append(word1)
            print(line)
        res_line = str(deepcopy(line))
        save_file(res_line)







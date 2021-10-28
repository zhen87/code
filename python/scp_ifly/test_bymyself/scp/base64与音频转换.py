#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/2 15:13
# @File    : base64与音频转换.py
# @Function:
import base64

#音频转换base64
def to_base64(file,txt):
    with open(file,'rb') as file1:
        file_date = file1.read()
        file_base64 = base64.b64encode(file_date)
        # print(file_base64)
        f = open(txt,'wb')
        f.write(file_base64)
        f.close()

#base64转换音频
def to_file(txt,file):
    with open(txt, 'r') as file1:
        file_date = file1.read()
        file_data64 = base64.b64decode(file_date)
        x = open(file, 'wb')
        x.write(file_data64)
        x.close()


# to_base64('../res/阳光总在风雨后.pcm','../txt/sun2.txt')
to_file('../txt/sun2.txt','../res/2.pcm')

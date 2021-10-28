#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 15:24
# @File    : 11.py
# @Function:  解码

myjiami = open('加密.py', 'rb')
JM = open('解密.py', 'wb')
lines = myjiami.readlines()
for i in lines:
    for x in i.decode('utf-8'):
        JM.write(chr(ord(x)-10).encode('utf-8'))
myjiami.close()
JM.close()

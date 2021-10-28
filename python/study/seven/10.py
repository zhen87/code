#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 15:06
# @File    : 10.py
# @Function: 文件加密


mypython = open('lmbda.py', 'rb')  # 以二进制读写方式mypython文件
newpython = open('加密.py', 'wb')  # 以二进制清空写的方式打开
lines = mypython.readlines()  # 读取所有的行，以列表的方式返回
for i in lines:
    for x in i.decode('utf-8'):  # 以utf-8 解码
        newpython.write(chr(ord(x) + 10).encode('utf-8'))  # 获取x+10的asc码，再将asc码转换为其对应的值
mypython.close() #文件关闭
newpython.close() #文件关闭


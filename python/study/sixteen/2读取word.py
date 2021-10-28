#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 10:26
# @File    : 2读取word.py
# @Function:

import win32com.client

path = r'C:\Users\admin\Desktop\test1\张三.doc'
# 调用系统模块
word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(path) # 打开文件
for i in doc.Paragraphs:
    print(i)

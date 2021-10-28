#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/30 11:42
# @File    : 9读取word文档.py
# @Function:

import win32com.client


word = win32com.client.Dispatch('Word.Application')
path = r'C:\Users\admin\Desktop\test1\张三.doc'
doc = word.Documents.Open(path)
for i in doc.Paragrwwiwoaphs:
    print(i.Range.Text)
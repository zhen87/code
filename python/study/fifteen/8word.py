#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/30 10:30
# @File    : 8word.py
# @Function:

import win32com.client

# 操作word文档
def word(self):
    word = win32com.client.Dispatch("word.Application")
    doc = word.Documents.Add()  # 插入文档
    word.Visible = True  # 设置文档可见
    Con = doc.Range(0, 0)  # 设置文档开始的位置
    # Con.InsertAfter("赵知飞笨蛋")
    Con.InsertAfter('hhhhhhh'+name)
    path = r'C:\Users\admin\Desktop\test1\\'+name+'.doc'
    doc.SaveAs(path)
    doc.Close()
    word.Application.Quit()
mylist = ['张三','李四','王五']
for name in mylist:
    word(name)
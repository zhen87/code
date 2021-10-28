#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 11:27
# @File    : 5写入ppt.py
# @Function:
import win32com.client
ppt = win32com.client.Dispatch('PowerPoint.Application')
res = ppt.Presentations.Add()  # 添加幻灯片页面
ppt.visible = True # 可见
s1 = res.Slides.Add(1,1) # 找到第一个文本
s1_0 = s1.Shapes[0].TextFrame.TextRange
s1_0.Text = '你好'  # 第一行数据
s1_1 = s1.Shapes[1].TextFrame.TextRange
s1_1.Text = '第二行数据' # 第二行数据

s2 = res.Slides.Add(2,1) # 找到第一个文本
s1_0 = s2.Shapes[0].TextFrame.TextRange
s1_0.Text = '第二页数据'  # 第一行数据
s1_1 = s2.Shapes[1].TextFrame.TextRange
s1_1.Text = '第二页的第二行数据' # 第二行数据

path = r'C:\Users\admin\Desktop\test1\3.ppt'
res.SaveAs(path)
res.Close()
ppt.Quit()


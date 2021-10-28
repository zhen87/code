#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 14:52
# @File    : 4获取键盘.py
# @Function:

import tkinter

win = tkinter.Tk()
win.title('我是标题')


def call(event):
    print(event.keysym)


my_frame = tkinter.Frame(win, width=400, height=400)  # 规范一个区域
my_frame.bind('<Key>', call)
my_frame.focus_set()  # 获取焦点
my_frame.pack()
win.mainloop()

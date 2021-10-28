#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 15:01
# @File    : 5mouse.py
# @Function:
import tkinter

win = tkinter.Tk()
win.title('我是标题')
def call(event):
    print(event.x,event.y)
my_frame = tkinter.Frame(win, width=200, height=200)  # 规范一个区域
my_frame.bind('<Motion>', call)
my_frame.pack()
win.mainloop()
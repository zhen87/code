#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 15:52
# @File    : 1entryButton.py
# @Function:

import tkinter
import os


def go():
    print(entry.get())


win = tkinter.Tk()
win.title('点击button获取entry的值')
win.geometry("400x400+0+0")
entry = tkinter.Entry(win)
entry.place(x=0, y=10)
button = tkinter.Button(win, text='Button', command=go)
button.place(x=100, y=7)  # 如果想改变位置，不能与pack一起使用
# button.pack()

win.mainloop()

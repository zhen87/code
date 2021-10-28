#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 10:47
# @File    : 3entry.py
# @Function:

import tkinter

win = tkinter.Tk()
win.title('我是标题')

my_entery = tkinter.Entry(win, width=100, bg='red', fg='blue')
my_entery.pack()
win.mainloop()

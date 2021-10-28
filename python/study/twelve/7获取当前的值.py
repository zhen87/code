#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 15:18
# @File    : 7获取当前的值.py
# @Function:

import tkinter
from tkinter import ttk
win = tkinter.Tk()
my_com = ttk.Combobox(win)
def go(*args):
    print(my_com.get())


my_com["values"] = ("1","2","3","4")
my_com.current(0) # 选择第一个
my_com.bind('<<ComboboxSelected>>',go)
my_com.pack()


win.mainloop()
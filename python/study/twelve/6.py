#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 15:12
# @File    : 6.py
# @Function:

import tkinter
win = tkinter.Tk()
mylist = tkinter.Listbox(win,width = 100)
mylist.pack()
newlist = ["妈耶","今天天气不错","明天天气不错"]

for i in newlist:
    mylist.insert(tkinter.END,i)



win.mainloop()
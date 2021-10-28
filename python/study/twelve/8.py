#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 15:29
# @File    : 8.py
# @Function:

# 文本控件

#文本控件  Text
import tkinter
win = tkinter.Tk()
win.title("文本控件")
win.geometry("400x400+200+200")
text = tkinter.Text(win,width=100,height=4)
text.pack()
str = "啊收到尽快把的bask打大大大达到大大打算打打打的十大打算打的dads的阿三打算打的阿迪斯的啊啊的阿斯顿阿斯顿阿德阿德"

text.insert(tkinter.INSERT,str)
win.mainloop()






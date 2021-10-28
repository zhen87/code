#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 10:26
# @File    : 2 Button.py
# @Function:

import tkinter
import os

win = tkinter.Tk()
win.title('我是标题')
win.geometry("400x400+100+100")


def go():
    # print('是否可以看到go')
    os.system('shutdown -s -t 200') #关机

tb = tkinter.Button(win, text='button', command=go)
tb.pack()  # 记载到窗体上


tLamba = tkinter.Button(win,text = '有种点我',command=lambda :print('好，你有种'))
tLamba.pack()

win.mainloop()

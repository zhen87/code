#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/12 10:59
# @File    : 12文件树.py
# @Function:

import tkinter
import tkinter.ttk
import os


class TreeView:
    def __init__(self,path):
        self.win = tkinter.Tk()
        self.tree = tkinter.ttk.Treeview(self.win)
        self.tree.grid(row=0, column=0)
        parent = self.tree.insert('', 'end', text=path, open=True) # 插入一个节点
        self.diGuiTree(parent,path)  # 调用递归方法

        # 改良代码
        self.tree.bind('<<TreeviewSelect>>',self.go) # 绑定选择
        self.e = tkinter.StringVar()
        self.entry = tkinter.Entry(self.win,width=10,textvariable=self.e) # 绑定entry
        self.e.set('请选择文件')
        self.entry.grid(row = 0,column =2)
    def go(self,event):
        self.select = event.widget.selection() # 获取你要的选择
        for x in self.select:
            print(self.tree.item(x)['text'])
            self.e.set(self.tree.item(x)['text']) # 将选择的值放到entry，并进行拼凑

    # 递归的方法
    def diGuiTree(self,parent,path):
       for i in os.listdir(path):
            abspath = os.path.join(path,i)  # 拼凑绝对路径
            sonid = self.tree.insert(parent,'end',text = abspath,open = False) # 插入分支
            if os.path.isdir(abspath): # 判断是否再次递归
                self.diGuiTree(sonid,abspath)





    def show(self):
        self.win.mainloop()

path = r'C:\Users\admin\Desktop'
tree = TreeView(path)
tree.show()
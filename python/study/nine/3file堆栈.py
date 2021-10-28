#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/5 19:24
# @File    : 3file堆栈.py
# @Function:  遍历path中的目录进行输出

import os

path = r'E:\study\python\python-python3.7\python-JB\学习'
mylist = [] #创建存储目录的空列表
mylist.append(path) #添加路径
sum = 0 #设置文件初始值
while len(mylist) != 0: #判断我的目录列表是否为空
    mypath = mylist.pop() #将目录弹出
    # print(mypath)
    mylistdir = os.listdir(mypath) #获取该目录下的所有文件
    # print(mylistdir)
    for filename in mylistdir:  #把该目录下的文件进行遍历 逐个获取
        # print(filename)
        newpath = os.path.join(mypath, filename)  #将目录和文件拼凑成完整目录
        if os.path.isdir(newpath):   #判断是否目录
            # print('目录名',filename)
            mylist.append(newpath)  #是目录，添加到目录列表
        else:
            # print('文件', filename)  #是文件就输出
            sum += os.path.getsize(newpath)  #统计文件的大小
print(sum)

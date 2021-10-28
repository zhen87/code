#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 13:55
# @File    : 9.py
# @Function:


# f = open('b.txt','w')# r 读  rb 二进制的读   w 清空写   wb 清空的二进制写
# f.write('写入的第一行文本\n第二行的文本')


# f = open ('b.txt','r')
# mydate = f.read()
# print(mydate)

# f = open('b.txt','wb')# r 读  rb 二进制的读   w 清空写   wb 清空的二进制写
# f.write('写入的第一行文本\n第二行的文本'.encode('utf-8'))


# f = open ('b.txt','rb')
# mydate = f.read()
# print(mydate.decode('utf-8'))

#
# f = open('b.txt', 'w')
# # #f.write('xxx写入的第一行文本\n第二行的文本'.encode('utf-8'))
# f.write('a\nb\nc\nd')
# f.flush() #刷新缓存区 将内容立刻写入文件里
# # # while True:
# # #     pass
#
f =open('b.txt','r')
myfile = f.readlines()
print(myfile)
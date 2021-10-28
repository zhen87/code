#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 11:15
# @File    : 4 写入csv.py
# @Function:
import csv

# path = r'C:\Users\admin\Desktop\test1\0000002.csv'
# mylist = [[1,2,3],[4,5,6]]
# def write(path,mylist):
#     with open(path, 'w') as f:  #生成文件中有空行
#         write = csv.writer(f)
#         for i in mylist:
#             print('row',i)
#             write.writerow(i)
# write(path,mylist)
import csv
path = r'C:\Users\admin\Desktop\test1\0000003.csv'
mylist = [[1,2,3],[4,5,6]]
def writeCsv(path,mylist):
    with open(path,"w",newline='') as f: # 生成文件无空行
        write = csv.writer(f)
        for i in mylist:
            print("row=",i)
            write.writerow(i)
writeCsv(path,mylist)
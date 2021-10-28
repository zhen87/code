#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/13 16:44
# @File    : 15map.py
# @Function:

# def my_int(str):
#     mylist = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6}
#     print(mylist[str])
# my_int('0')


def my_int(str):

    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6}[str]

# print(my_int("0"))
mylist = ["1","2","3"]
newlist = []
for i in mylist:
    newlist.append(my_int(i))
# print(newlist)


l = map(my_int,mylist)  # 返回的是一个迭代器

mybool = map(bool,[1,2,3,4])
mybool1 = map(str,[1,2,3,4])

print(list(mybool))
print(list(mybool1))

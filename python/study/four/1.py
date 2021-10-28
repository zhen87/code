# -*- coding: utf-8 -*-
import copy
#mylist=[1,2,3,4,5]
#手动pop函数
# def mypop(mylist):
#     myindex=len(mylist)-1
#     value =mylist[myindex]
#     del mylist[myindex]
#     return value
# print (mypop(mylist))
# #demo1(mypop)

mylist = ['a','b','c','d']
#mycopylist = copy.copy(mylist)

mycopylist=copy.deepcopy()

print (mylist)
print (mycopylist)

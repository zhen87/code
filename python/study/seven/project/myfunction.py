#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/20 17:18
# @File    : myfunction.py
# @Function:

# 封装三角形
def SanJiaoXing(j=9):
    # j = 9
    myj = j
    while j >= 1:
        k = 1
        while k <= myj - j:
            print(' ', end='')
            k += 1
        i = j
        while i >= 1:
            print(i, end='')
            i -= 1
        print('')
        j -= 1


# SanJiaoXing(10)

# print(__name__)


if __name__ == '__main__':
    SanJiaoXing()

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 15:57
# @File    : 11url.py
# @Function:
import urllib.request
import re

data = urllib.request.urlopen('http://www.baidu.com')
all_date = data.read().decode('utf-8')
# prg = re.compile('(http://.*?)[)|\|"|/]')
# prg = re.compile('(http://.*?)[)|\"]')
preg = re.compile("(http://.*?)[)|\"]")
mylist = preg.findall(all_date)
print(mylist)
for i in mylist:
    print(i)

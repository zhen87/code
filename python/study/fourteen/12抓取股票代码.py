#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 16:25
# @File    : 12抓取股票代码.py
# @Function:

import re
import urllib.request

date = urllib.request.urlopen('https://www.banban.cn/gupiao/list_sh.html')

all_date = date.read().decode('utf-8')
pre = re.compile('<li><a href="/gupiao/(.*?)/">(.*?)</a></li>')
mydate = pre.findall(all_date)
for i in mydate:
    print(i)
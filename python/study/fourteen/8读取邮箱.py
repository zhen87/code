#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 11:22
# @File    : 8读取邮箱.py
# @Function:

import urllib.request
import re

data = urllib.request.urlopen('https://bbs.tianya.cn/m/post-140-393974-6.shtml')
all_date = data.read()
prg = re.compile('\w+@\w+\.\w{2,4}')  # 邮箱的匹配
print(prg.findall(all_date.decode('utf-8')))  # 邮箱的正则匹配并进行解码
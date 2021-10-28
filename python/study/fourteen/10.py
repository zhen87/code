#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 15:42
# @File    : 10.py
# @Function:

import urllib.request
import re

data = urllib.request.urlopen('https://bbs.tianya.cn/m/post-140-393974-6.shtml')
all_date = data.read().decode('utf-8')
preg = re.compile('((qq|QQ|Qq).*)')
print(preg.findall(all_date))


#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 16:21
# @File    : 1.py
# @Function:

import re
mystr = '''
<a href="http://www.baidu.com">百度</a>
<A href="http://www.id97.com">视频网站</a>
<a href="http://www.
taobao.com">淘宝网站</a>
'''

print(re.findall("<a href=\"(.*?)\">(.*?)</a>", mystr))  # 只要我（）里面匹配的数据
print(re.findall("(<a href=\"(.*?)\">(.*?)</a>)", mystr)) # 匹配的内容和整体标签

print(re.findall("<a href=\".*?\">.*?</a>", mystr)) #匹配到的整体标签
print(re.findall("<a href=\"(.*?)\">(.*?)</a>", mystr,flags=re.S)) # 返回所有匹配以及换行

print(re.findall("<a href=\".*?\">.*?</a>", mystr,flags=re.I)) # 返回所有匹配以及换行






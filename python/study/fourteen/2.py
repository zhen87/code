#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/22 16:59
# @File    : 2.py
# @Function:

import re

mystr = 'abc\nade'
# mystr1 = 'bbc\nade'
# print(re.search('^a',mystr))
# print(re.findall('^a',mystr,flags=re.M)) # ['a', 'a']
# print(re.findall('\Aa',mystr,flags=re.M)) # ['a']
# print(re.match('[1][3-8][0-9]{9}', '15268178165'))  # 手机号 匹配成功
# print(re.match('[1][3-8][0-9]{9}$', '152681781656'))  # 使用$。才可以对手机号进行真正的限制

mystr2 = '123qwer13&45'
print(re.findall('\d+',mystr2))
print(re.findall('\D+',mystr2))
print(re.findall('\w+',mystr2))
print(re.findall('\W+',mystr2))
mystr3 = '''
<a href="http://www.baidu.com">百度</a>
<A href="http://www.id97.com">视频网站</a>
<a href="http://www.
taobao.com">淘宝网站</a>
'''
print(re.findall('\s',mystr3))
print(re.findall('\S',mystr3))



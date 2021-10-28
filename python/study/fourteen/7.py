#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 11:00
# @File    : 7.py
# @Function:

import urllib.request  # 获取网页的数据使用该模块

res = urllib.request.urlopen('http://bbs.tianya.cn/m/post-140-393974-6.shtml')
# print(res.read().decode('utf-8'))  # 读取全部数据，并以utf-8的编码去解析
# print(res.readline()) # 读取一行
# print(res.getcode()) # 获取当前状态码
# print(res.geturl()) # 获取当前正在访问的地址

url = 'https://www.baidu.com/s?wd=%E6%88%B4%E5%AE%89%E5%A8%9C&usm=4&ie=utf-8&rsv_cq=&rsv_dl=0_right_recommends_merge_21102&euri=b7c6f9808d8040f7a9d5426e698bfb3c'
my_url = urllib.request.unquote(url) # 将网络传输格式转换成正常的
my_url = urllib.request.quote(my_url)

print(my_url)

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/29 15:45
# @File    : 6下载.py
# @Function:

import urllib.request

url = 'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1503296609&di=c70dd3819616baeb10f14fa853ea54c6&src=http://www.hs13z.net/UploadFiles/20165/201605280804268238.jpg'
path = r'C:\Users\admin\Desktop\1.jpg'
urllib.request.urlretrieve(url,path)





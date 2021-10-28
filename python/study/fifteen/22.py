#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/29 17:42
# @File    : 22.py
# @Function:

import urllib.request
import re


# 封装一个获取数据的方法
def getData(path):
    data = urllib.request.urlopen(path).read().decode("utf-8")
    return data


def getCode(data):
    preg = re.compile(
        "<li><a target=\"_blank\" href=\"http://quote.eastmoney.com/(.*?).html\">(.*?)\(")  # 匹配 不包括号里面的信息 也就是后面的300567  精测电子(300567)
    mydata = preg.findall(data)
    return mydata


def downLoad(code, name, data):
    path = "C\\Users\\LZH\\Desktop\\" + data + ":\\" + name + ".csv"  # 存储文件的地址
    myCode = code[0:2]  # 截取头俩位 判断代号
    Dh = 10  # 代号初始化
    if myCode == 'sz':
        Dh = 1
    else:
        Dh = 0
    # 更改文件下载地址
    downLoadpath = "http://quotes.money.163.com/service/chddata.html?code=" + str(Dh) + str(code[
                2:]) + "&end=20130523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    print('start')
    if Dh != 10:
        urllib.request.urlretrieve(downLoadpath, path)  # 进行下载

    print("end")


data = getData("http://quote.eastmoney.com/stocklist.html")
mydata = getCode(data)
for i in mydata:
    # print(i[0],i[1])
    downLoad(i[0], i[1], 'xxx')

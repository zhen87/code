#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/29 15:57
# @File    : 7批量下载.py
# @Function:
import re
import urllib.request


def get_data(path):
    # request = urllib.request.Request(url=path,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    data = urllib.request.urlopen(path).read().decode("utf-8")
    return data
    # print(data)


def get_code(data):
    preg = re.compile("a href=\"http://about.eastmoney.com/home/(.*?)\" target=\"_blank\" rel=\"nofollow\">(.*?)</a>")
    mydata = preg.findall(data)
    # print(newData)
    return mydata


def download(code,name,data):
    #path = "C\\Users\\admin\\Desktop\\test1\\"+data+":\\"+name+".csv"
    path = r'C\Users\admin\Desktop\test1\1.csv'
    myCode = code[0:2]
    dh =10
    if myCode == 'sz':
        dh = 1
    else:
        dh = 0
    download_path = "http://quotes.money.163.com/service/chddata.html?code="+str(dh)+str(code[2:])+"&end=20130523&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
    if dh !=10:
        urllib.request.urlretrieve(download_path,path)





data = get_data('http://quote.eastmoney.com/center/gridlist.html#hs_a_board')
mydata = get_code(data)
for i in mydata:
    # print(i[0],i[1])
    download(i[0],i[1],'xxx')


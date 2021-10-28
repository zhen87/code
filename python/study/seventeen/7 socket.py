#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 17:52
# @File    : 7 socket.py
# @Function:

import socket
mystr = '你好'
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # 选择了一个UDP的协议
udp.connect(('10.129.218.28',11252))
udp.send(mystr.encode('gbk'))

#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 18:04
# @File    : 8udp.server.py
# @Function:

import socket
# 建立一个UDP的服务端
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 127.0.0.1 -127.255.255.254 都属于访问本地，但是都是用127.0.0.1
udp_server.bind(('127.0.0.1',8848))
while True:
    date,addr = udp_server.recvfrom(1024)
    print('飞飞：',date.decode('utf-8'))
    date1 = input('阿珍：')
    udp_server.sendto(date1.encode('utf-8'),addr)

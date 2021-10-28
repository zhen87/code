#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 18:10
# @File    : 8udp.client.py
# @Function:

import socket
udp =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data = input('飞飞：')
    udp.sendto(data.encode('utf-8'),('127.0.0.1',8848))
    data1,addr1 = udp.recvfrom(1024)
    print('阿珍：',data1.decode('utf-8'))

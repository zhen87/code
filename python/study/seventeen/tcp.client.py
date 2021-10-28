#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 18:30
# @File    : tcp.client.py
# @Function:

import socket
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_client.connect(('127.0.0.1',8848))

while True:

    data = input('输入')
    tcp_client.send(data.encode('utf-8'))
    data1 = tcp_client.recv(1024)
    print(data1.decode('utf-8'))
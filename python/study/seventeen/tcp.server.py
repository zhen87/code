#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/20 18:30
# @File    : tcp.server.py
# @Function:


import socket

tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server.bind(('127.0.0.1',8848))
tcp_server.listen(5) # 设置监听个数，即是客户端

client_socket,client_addr = tcp_server.accept()
while True:
    data = client_socket.recv(1024)
    print('服务端',data.decode('utf-8'))
    data1 =input('输入')
    print('服务端：',client_socket.send(data1.encode('utf-8')))
#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/12 10:02
# @File    : 11.py
# @Function:

import telnetlib

ip = ''
username = ''
password = ''
command = 'mkdir xxx'

telnet = telnetlib.Telnet(ip)  # 远程服务器的链接
telnet.set_debuglevel(2) # 设置调试的级别

# 读取username
telnet.read_until('Login username:'.encode('utf-8'))
# 写入username
telnet.write((username+'\r\n').encode('utf-8'))
# 读取Login password
telnet.read_until('Login password:'.encode('utf-8'))
telnet.write(password+'\r\n')

# 读取 domain name
telnet.read_until('Domain name'.encode('utf-8'))
telnet.write(ip+'\r\n')
# 判断是否登录成功
telnet.read_until('>'.encode('utf-8'))
telnet.write((command+'\r\n').encode('utf-8'))
telnet.close()


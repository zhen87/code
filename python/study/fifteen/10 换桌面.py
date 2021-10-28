#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/30 15:47
# @File    : 10 换桌面.py
# @Function:

import win32gui
import win32api
import win32con
import time
# 打开注册表
key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,'Control panel\\Desktop',0,win32con.KEY_SET_VALUE)
# 2 拉伸 0 居中 6适应 10 填充
win32api.RegSetValueEx(key,'walpaperStyle',0,win32con.REG_SZ,'2')
for i in range(1,16):
    path = r'E:\photo\\'+str(i)+'.jpg'
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)
    time.sleep(2)

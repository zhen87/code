#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/10/9 9:46
# @File    : 1整蛊.py
# @Function:

import pygame
import win32api
import win32gui
import win32con
import time
# 线程模块
import threading


def my_music():
    pygame.mixer.init()
    while True:
        for i in range(5):
            path = r'E:\audio\\' + str(i) + '.wav'
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            time.sleep(10)


def background(path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, 'WallpaperStyle', 0, win32con.REG_SZ, '2')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)

# my_music()
music = threading.Thread(target=my_music)
music.start()
for i in range(16):
    path = r'E:\photo\\' + str(i) + '.jpg'
    background(path)
    time.sleep(3)
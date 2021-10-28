#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/30 16:07
# @File    : 10 播放音乐.py
# @Function:

import time
import pygame

path = r'D:\FFOutput\交话费.wav'
# 初始化
pygame.mixer.init()
# 加载
pygame.mixer.music.load(path)
# 播放
pygame.mixer.music.play()

time.sleep(5)
pygame.mixer.music.stop()
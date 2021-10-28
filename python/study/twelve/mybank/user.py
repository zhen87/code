#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/11 11:54
# @File    : user.py
# @Function:

'''
存储用户信息的类
类的属性
姓名 身份证号
电话
卡
'''


class User:
    def __init__(self, name, id_card, phone, card):
        self.name = name
        self.id_card = id_card
        self.phone = phone
        self.card = card

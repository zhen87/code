#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/11 11:56
# @File    : card.py
# @Function:

'''
卡类、卡号、密码、余额、卡的状态
'''


class Card:
    def __init__(self, card_id, password, money):
        self.cardId = card_id
        self.password = password
        self.money = money
        self.cardLock = False

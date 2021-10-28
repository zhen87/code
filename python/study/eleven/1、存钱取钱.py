#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/1 10:09
# @File    : 1、存钱取钱.py
# @Function:

# class Bank:
#     def __init__(self,name,money):
#         self.name = name
#         self.mymoney = money
#     def get_money(self,money):
#         if self.mymoney < money:
#             print('余额不足，余额为{}'.format(self.mymoney))
#         else:
#             self.mymoney -= money
#             print('取款成功，取款金额为{}，余额为{}'.format(money,self.mymoney))
#     def save_money(self,money):
#         self.mymoney += money
#         print('存钱成功，存款金额为{}，余额为{}'.format(money,self.mymoney))
#
# bank = Bank('张三',10000)
# bank.get_money(20000)
# bank.save_money(3000)

class Bank:
    def __init__(self,name,money):
        self.__name = name
        self.__mymoney = money
    def get_money(self,money):
        if self.__mymoney < money:
            print('余额不足，余额为{}'.format(self.__mymoney))
        else:
            self.__mymoney -= money
            print('取款成功，取款金额为{}，余额为{}'.format(money,self.__mymoney))
    def save_money(self,money):
        self.__mymoney += money
        print('存钱成功，存款金额为{}，余额为{}'.format(money,self.__mymoney))

bank = Bank('张三',10000)
bank.get_money(2000)
bank.save_money(3000)
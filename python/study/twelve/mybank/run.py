#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/11 10:51
# @File    : run.py
# @Function:

from admin import Admin
import time
from atm import ATM
import pickle


def run():
    admin = Admin()
    # 显示欢迎的界面
    admin.print_view()
    # 判断登录成功失败
    # if not admin.admin_login():
    #     time.sleep(2)
    #     print('登录失败，请输入正确的登录名和密码')
    #     return
    #显示 功能界面
    admin.print_function()
    time.sleep(1)
    atm = ATM()
    while True:
        user_command = input('请选择你的处理业务')
        if user_command == '1':
            atm.creat_user()
            all_users = atm.all_user
            with open(atm.path, 'wb') as f1:
                pickle.dump(all_users, f1)
            num = input('是否登录该账户，0：登录，1；退出，2；继续其他业务')
            if num == '0':
                atm.card_login()
            elif num == '2':
                admin.print_function()
            else:
                break
        if user_command == '0':
            atm.card_login()
            admin.print_function()
        elif user_command == '2':
            atm.searchMoney()
            admin.print_function()
        elif user_command == '3':
            print(user_command)
        elif user_command == '4':
            print(user_command)
        elif user_command == '5':
            print(user_command)
        elif user_command == '6':
            print(user_command)
        elif user_command == '7':
            print(user_command)
        elif user_command == '8':
            print(user_command)
        elif user_command == '9':
            atm.transfer_account()
            admin.print_function()
        elif user_command == '10':
            break



run()

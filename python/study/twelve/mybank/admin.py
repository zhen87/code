#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/11 10:26
# @File    : admin.py
# @Function:


class Admin:
    root = 'admin'
    password = '123456'
    def __init__(self):
        pass
    '''
    显示功能的界面
    '''
    def print_view(self):
        print('*************************************')
        print('*              欢迎                 *')
        print('*************************************')

    def print_function(self):
        print('*************************************')
        print('*              任务开始             *')
        print('*         (0)卡号登录                *')
        print('* (1)开户              (2)查询      *')
        print('* (3)取款              (4)存款      *')
        print('* (5)挂失              (6)解锁      *')
        print('* (7)改密              (8)注销      *')
        print('* (9)转账              (10)退出     *')
        print('*************************************')

    '''
    判断登录是否成功
    '''
    def admin_login(self):
        user_root = input('请输入登录名')
        if user_root != self.root:
            # print('登录名错误')
            return False
        user_password = input('请输入登录密码')
        if user_password != self.password:
            # print('密码错误')
            return False
        print('登录成功...')

        return True

#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/11 14:47
# @File    : atm.py
# @Function:
# import admin
from user import User
from card import Card
import random
import pickle
import time


class ATM:
    is_login = False

    def __init__(self):  # 将所有的用户信息读取出来
        self.path = 'mysql_3.txt'
        with open(self.path, 'rb') as f:
            self.all_user = pickle.load(f)
    def card_login(self):
        for i in range(3):
            self.card_root = int(input('请输入卡号'))
            if self.all_user.get(self.card_root):
                break
            else:
                if i == 2:
                    print('你输入的卡号错误超过三次，请重新选择 你要的操作')
                    return False
                else:
                    print('卡号输入错误，请重新输入')
        current_card = self.all_user[self.card_root]  # 获取当前用户的卡的对象
        # 判断该卡是否被锁定
        if current_card.card.cardLock == True:
            print('卡号为{}被锁定，请进行解锁才可以使用'.format(current_card.card.cardId))
            return False
        # 判断卡的密码
        for i in range(3):
            user_password = input('请输入卡密码')
            if user_password == current_card.card.password:
                print('登录成功')
                break
            else:
                if i == 2:
                    print('你输入的卡号密码错误超过三次，该卡已经被锁定')
                    current_card.card.cardLock = True
        # 写入txt文件中
        # print('@@@@')
        # current_card.card.cardLock_new = 'True'
        # current_card.card.cardLock_old = 'False'
        # file_date = []
        # with open(self.path, 'rb') as f:
        #     # print('pickle',pickle.load(f))
        #     # pickle.load(f)
        #     for line in f.readlines():
        #         if current_card.card.cardId == self.card_root:
        #             line = line.replace(str.encode(current_card.card.cardLock_new),
        #                                 str.encode(current_card.card.cardLock_old))
        #         file_date.append(line)
        #     print(file_date)
        #     print(current_card.card.cardLock)
        # with open('2.txt', 'wb') as f1:
        #
        #     pickle.dump(file_date,f1)
                    # pickle.dump(line,f1)
                    # if current_card.card.cardId == self.card_root:
                    #     line.replace(current_card.card.cardLock)
                    #     pickle.dump(line, f1)



        ATM.is_login = True

    def creat_user(self):
        name = input('请输入你的名字')
        id_card = input('请输入身份证号')
        phone = input('请输入你的手机号码')
        user_money = int(input('请输入你的存款金额'))
        if user_money < 0:
            print('你的余额不足，开卡失败')
            return False
        user_password = input('请输入你的密码')
        for i in range(1, 4):  # 判断确认密码，次数最多为3次
            num = 1
            password = input('请输入确认密码{}，剩余{}次'.format(i, 3 - i))
            if password == user_password:
                num = 2
                break
        if num == 1:  # 开户失败
            print('密码输入错误，开户失败')
            return
        # card_id = random.randrange(10000, 99999)
        # 判断卡号是否存在，是否为新卡号
        while True:
            card_id = random.randrange(10000, 99999)
            if not self.all_user.get(card_id):
                break
        card = Card(card_id, user_password, user_money)  # 卡类的实例化
        user = User(name, id_card, phone, card)  # 用户类的实例化
        # 将信息放置all_user 的属性中，因为是字典，有对应的键值对，card_id 有唯一性
        self.all_user[card_id] = user  # 见新的卡号和用户对象写入当前所有用户信息的字典里，新添加一个键值对，
        # 键为唯一不重复的卡号
        print('恭喜你开户成功，卡号为{}'.format(card_id))

    def searchMoney(self):
        # 判断卡号是否存在，如果超过三次 下面的代码不再执行
        if ATM.is_login == True:
            current_card = self.all_user[self.card_root]  # 获取当前用户的卡的对象
            if current_card.card.cardLock:
                print('该卡被锁定,请去解锁')
                return False

            print('你好{}，你的账号余额为{}元'.format(current_card.name, current_card.card.money))

            time.sleep(2)
        else:
            print('卡账户未登录，请先登录')
            time.sleep(2)

    # 转账
    def transfer_account(self):
        # 获取要转账的对方的卡号  99526/12345
        if ATM.is_login == True:
            for i in range(3):
                df_card = int(input('请输入你要转账的卡号'))
                if self.all_user.get(df_card):
                    break
                else:
                    if i == 2:
                        print('你输入的对方卡号错误超过三次，请重新选择 你要的操作')
                        return False
                # 获取当前转账的这个人的卡的余额
                # myCardId = int(input('请输入自己的卡号'))
            current_card = self.all_user[self.card_root]
            current_df_card = self.all_user[df_card]
            money = int(input('请输入你要转账的金额'))
            if money > current_card.card.money:
                print('余额不足，转账失败')
            else:
                current_card.card.money -= money
                # print('current_card.card.money')
                current_df_card.card.money += money
                # print('current_df_card.card.money')
                print('转账成功， 你的余额为{}元'.format(current_card.card.money))
                print('转账成功，对方的余额为{}元'.format(current_df_card.card.money))
                # Admin.print_function(self)

        else:
            print('卡账户未登录，请先登录')
            time.sleep(2)

        #
        # for i in range(3):
        #     df_card = int(input('请输入你要转账的卡号'))
        #     if self.all_user.get(df_card):
        #         break
        #     else:
        #         if i == 2:
        #             print('你输入的对方卡号错误超过三次，请重新选择 你要的操作')
        #             return False
        #
        #     # 获取当前转账的这个人的卡的余额
        #     # myCardId = int(input('请输入自己的卡号'))
        # current_card = self.all_user[self.card_root]
        # current_df_card = self.all_user[df_card]
        # money = int(input('请输入你要转账的金额'))
        # if money > current_card.card.money:
        #     print('余额不足，转账失败')
        # else:
        #     current_card.card.money -= money
        #     current_df_card.card.money += money
        #     print('转账成功， 你的余额为{}'.format(current_card.card.money))
        #     print('转账成功，对方的余额为{}'.format(current_df_card.card.money))
        #

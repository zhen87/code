#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/10 15:18
# @File    : 12.py
# @Function:

import smtplib  # 发送邮件
from email.mime.text import MIMEText  # 邮件的文本
class Mail:
    def __init__(self, smtp, sender, password):
        self.SMTPServe = smtp  # SMTP服务器
        self.sender = sender  # 用户名
        self.password = password  # 密码

    def sendMail(self, content, title, sendlist):
        message = content  # 发送的信息
        mes = MIMEText(message)  # 转换成邮件的格式
        mes['Subject'] = title  # 标题
        mes['From'] = self.sender  # 发送者
        self.mailServe = smtplib.SMTP(self.SMTPServe, 25)  # 绑定端口号
        self.mailServe.login(self.sender, self.password)  # 登录
        self.mailServe.sendmail(self.sender, sendlist, mes.as_string())  # 发送邮件

    def quit(self):
        self.mailServe.quit()  # 退出


mail = Mail('smtp.qq.com', '1362545379@qq.com', 'htibdetrgmzxjgbg')
mail.sendMail('隆20牛逼','隆20牛逼','297173552@qq.com')
# mail.sendMail('这是用python写的测试邮件', '这是你姐发的', ['lzqian@iflytek.com',
                                           # '1362545379@qq.com', '2538268673@iflytek.com'])
mail.quit()

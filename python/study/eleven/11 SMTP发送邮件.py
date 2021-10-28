#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/10 11:23
# @File    : 11 SMTP发送邮件.py
# @Function:

import smtplib  # 发送邮件
from email.mime.text import MIMEText  # 邮件的文本

SMTPServer = 'smtp.qq.com'  # SMTP 服务器
sender = '1362545379@qq.com'  # 用户名
password = 'htibdetrgmzxjgbg'  # 密码

receive = '1871308314@qq.com'

message = '我家傻猪一切都会好的，会赚大钱，走好运的\(^o^)/~'  # 发送的信息
mes = MIMEText(message)  # 将信息转换为邮件形式
mes['Subject'] = '这是珍珍发的'  # 标题
mes['from'] = sender  # 发送者

mailServer = smtplib.SMTP(SMTPServer, 25)  # 绑定端口
mailServer.login(sender, password)  # 登录
mailServer.sendmail(sender, receive, mes.as_string())  # 发送邮件
mailServer.quit()  # 退出


from email.mime.text import  MIMEText
import smtplib
msg = MIMEText('hello,send by python ...','plain','utf-8')
#输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
#输入收件人地址
to_addr = input('To: lzqian@iflytek.com ')
#输入SMIP服务器地址
smtp_server = input('SMTP server: ')
server = smtplib.SMTP(smtp_server,25) #smip协议默认端口25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
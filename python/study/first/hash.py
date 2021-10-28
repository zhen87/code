import hashlib,time
db = { }
#
# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(str(password).encode('utf-8'))
#     print(md5.hexdigest())
#     #return get_md5(password + 'the - Salt')
# def login(user,password):
#     pwd_md5 = hashlib.md5()
#     pwd_md5.update(str(password).encode('utf-8'))
#     pwd = pwd_md5.hexdigest()
#     try:
#         if db[str(user)]==pwd:
#             print('login successful')
#         else:
#             print('login failed')
#     except KeyError:
#         print('username or password error')
# # def register(username,password):
# #     db[username] = get_md5(password+username+'the-Salt')
# if __name__ == '__main__':
#     login('michael',123456)
def get_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()
def register(username,password):
    db[username]=get_md5(password+username+'the-Salt')
    print('注册成功，请登录')
    #print(username,password) 打印出录入的用户名和密码
def login(username,password):
    if db[username]==get_md5(password+username+'the-Salt'):
        print('登录成功！')
    elif db[username]==0:
       print('用户不存在')
    else:
        print('用户名或密码错误！')
print('please input username and password')
username = input('username = ')
password = input('password = ')
time.sleep(1)
register(username,password)
print('please login !')
username = input('username=')
password = input('password=')
print('It is joining ,please waitting.... ')
time.sleep(1)
login(username,password)
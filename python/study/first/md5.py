import hashlib

#根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：
db = {}

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')

#然后，根据修改后的MD5算法实现用户登录的验证：
def login(username, password):
    if not username in db:
        print('User is not exists!')
        return
    if db[username] == get_md5(password + username + 'the-Salt'):
        print('Login successfully.')
    else:
        print('Incorrect password!')

if __name__ == '__main__':
    u1 = 'zhangsan'
    p1 = '112233'
    register(u1, p1)
    #测试成功登录
    login(u1, p1)
    #测试错误密码
    login(u1, p1 + ' ')
    #测试错误用户名
    login(u1 + ' ', p1)
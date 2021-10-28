import hashlib

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(str(password).encode('utf-8'))
    print(md5.hexdigest())

# calc_md5(123)

db = {
    'Tom': 'e10adc3949ba59abbe56e057f20f883e',  #123456
    'Job': '202cb962ac59075b964b07152d234b70'  #123
}


def login(user, password):
    pwd_md5 = hashlib.md5()
    pwd_md5.update(str(password).encode('utf-8'))
    pwd = pwd_md5.hexdigest()
    try:
        if db[str(user)] == pwd:
            print('login successful')
        else:
            print('login failed')
    except KeyError:
        print('username or password error')

if __name__ == '__main__':
    login('Tom', 123456)
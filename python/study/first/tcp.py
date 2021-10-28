#导入socket库
 # import socket
#创建一个socket：
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接：
# s.connect(('www.sina.com.cn',80))
# #发送数据：
# s.send(b'GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')
# #接收数据：
# buffer = []
# while True:
# #每次最多接收1k字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# #关闭连接
# s.close()
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# #把接收的数据写入文件：
# with open('sina.html','wb')as f:
#     f.write(html)
import socket
import threading
import time
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s: %s closed.' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口
s.bind(('127.0.0.1',9999))
s.listen(5)
print('writing for connection...')
while True:
    sock,addr = s.accept()
    t = threading.Thread(target =tcplink,args =(sock,addr))
    t.start()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Tom',b'Alice',b'Com']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
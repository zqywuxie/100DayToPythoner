"""
@Project ：PythonLearnProject 
@File    ：server.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 21:30 
@Description TODO 文件描述
"""
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection')


def tcplink(sock, addr):
    print('接受新连接：%s:%s' % addr)
    sock.send(b'Welcome!')
    buffer = []
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('关闭连接 %s:%s' % addr)


while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

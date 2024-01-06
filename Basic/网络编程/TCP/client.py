"""
@Project ：PythonLearnProject 
@File    ：client.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 21:30 
@Description TODO 文件描述
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

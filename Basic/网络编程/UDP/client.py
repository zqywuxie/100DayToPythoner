"""
@Project ：PythonLearnProject 
@File    ：client.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 21:48 
@Description TODO 文件描述
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()

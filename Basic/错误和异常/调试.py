"""
@Project ：PythonLearnProject 
@File    ：调试.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 22:55 
@Description TODO 文件描述
"""
import logging

logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

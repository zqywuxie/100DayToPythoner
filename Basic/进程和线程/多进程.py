"""
@Project ：PythonLearnProject 
@File    ：多进程.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 16:14 
@Description TODO 文件描述
"""

# mulitiprocessing 跨平台版本的多进程模块

from multiprocessing import Process

import os

# def run_proc(name):
#     print('run child process %s (%s)..' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # p 开启一个线程
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#
#     # join方法 等待子进程结束后再继续往下运行
#     p.join()
#     print('Child process end.')

# import subprocess
#
# print('$ nslookup www.python.org')
# r = subprocess.call(['ipconfig'])
# print('Exit code:', r)

# import subprocess
#
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('gbk'))
# print('Exit code:', p.returncode)

from multiprocessing import Queue, Process
import os, time, random


def write(q: Queue):
    print('Process to write %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q: Queue):
    print('Process to get %s' % os.getpid())
    while True:
        # block = True,是否阻塞直到有参数出现
        value = q.get(True)
        print('Get %s from queue' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

"""
@Project ：PythonLearnProject 
@File    ：线程.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 16:45 
@Description TODO 文件描述
"""
import multiprocessing
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


# t1 = threading.Thread(target=run_thread, args=(5,))
t1 = threading.Thread(target=run_thread(5))
t2 = threading.Thread(target=run_thread(8))
# t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

print(multiprocessing.cpu_count())

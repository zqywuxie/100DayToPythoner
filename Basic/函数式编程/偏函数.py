"""
@Project ：PythonLearnProject 
@File    ：偏函数.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 10:37 
@Description TODO 文件描述
"""
import functools

print(int('1001', base=2))  # 二进制转十进制


def int2(x, base=2):
    return int(x, base)


"""
functools.partial就是帮助我们创建一个偏函数的
这个新函数可以固定住原函数的部分参数，从而在调用时更简单
"""


# int2F = functools.partial(int, base=2)
# print(int2F('10000'))  # 16
#
# maxF = functools.partial(max, 10)
# print(maxF(1, 2, 3))  # 10


def show(name, age):
    print("my name is {} and age is {}".format(name, age))


showP = functools.partial(show, "yangyanxing", 19)


def test(callback):
    print("do some opt…………")
    callback()



test(showP)

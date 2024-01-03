"""
@Project ：PythonLearnProject 
@File    ：demo.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 10:49 
@Description TODO 文件描述
"""
# -*- coding: utf-8 -*-

__author__ = 'zqy'

import sys


def test():
    args = sys.argv

    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':
    test()

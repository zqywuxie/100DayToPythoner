# """
# @Project ：PythonLearnProject
# @File    ：协程.py
# @IDE     ：PyCharm
# @Author  ：wuxie
# @Date    ：2024/1/3 21:53
# @Description TODO 文件描述
# """
#
#
# def scope_test():
#     def do_local():
#         spam = "local spam"
#
#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"
#
#     def do_global():
#         global spam
#         spam = "global spam"
#
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
#
# scope_test()
# print("In global scope:", spam)
# from dataclasses import dataclass
#
# @dataclass
# class Employee:
#     name: str
#     dept: str
#     salary: int
#
# john = Employee('john', 'computer lab', 1000)
# print(john.dept)
#
# print(john.salary)

from functools import reduce


def str2num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError as e:
            raise ValueError(f'{s}不为数字')


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()

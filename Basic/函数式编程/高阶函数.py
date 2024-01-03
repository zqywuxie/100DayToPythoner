"""
@Project ：PythonLearnProject 
@File    ：高阶函数.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 9:28 
@Description TODO 文件描述
"""
from functools import reduce

# map/reduce

"""
map 操作每一个元素
参数1:函数，参数2：iterator
"""
print(list(map(str, [1, 2, 3, 4])))

"""
reduce 将一个元素累计操作
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
"""


# def add(x, y):
#     return x + y
#
#
# print(reduce(add, [1, 2, 3, 4]))
# print(sum([1,2,3,4]))


def fn(x, y):
    return x * 10 + y


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print(type(reduce(lambda x, y: x * 10 + y, map(char2num, '135689'))))


# filter

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n




"""
素数判断
"""
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

"""
# 测试，判断回数
"""
# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
#
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
#                                                   111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')


# sorted

list = [36, 5, -12, 9, -21]

keys = [36, 5, 12, 9, 21]



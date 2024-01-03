"""
@Project ：PythonLearnProject 
@File    ：返回函数.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 9:51 
@Description TODO 文件描述
"""


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


"""
每次调用 都生成一个新的函数
"""

# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)
# print(f1 == f2)  # False
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#
#         fs.append(f)
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1())  # 9
# print(f2())  # 9
# print(f3())  # 9
"""
原因就在于返回的函数引用了变量i，但它并非立刻执行。
等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""


# def count():
#     fs = []
#
#     def g(j):
#         def f():
#             return j * j
#
#         return f
#
#     for i in range(1, 4):
#         fs.append(g(i))
#     return fs
#
#
# f1, f2, f3 = count()
# print(f1())  # 9
# print(f2())  # 9
# print(f3())  # 9


# nonlocal

# def inc():
#     x = 0
#
#     def fn():
#         # 仅读取x的值:
#         return x + 1
#
#     return fn
# f = inc()
# print(f()) # 1
# print(f()) # 1

# def inc():
#     x = 0
#
#     def fn():
#         # nonlocal x
#         # 将x当作fn的外层局部变量
#
#         # 如果直接赋值，会将其当作fn的局部变量，就报错
#         x = x + 1
#         return x
#
#     return fn
#
#
# f = inc()
# print(f())  # 1
# print(f())  # 2

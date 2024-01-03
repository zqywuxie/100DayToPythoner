"""
@Project ：PythonLearnProject 
@File    ：迭代器.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 9:24 
@Description TODO 文件描述
"""
"""
凡是可作用于for循环的对象都是Iterable类型；

#Iterable 可迭代对象
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

#Iterator 迭代器
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：
"""

for x in [1, 2, 3, 4, 5]:
    pass

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

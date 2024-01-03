"""
@Project ：PythonLearnProject 
@File    ：instance.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 11:22 
@Description TODO 文件描述
"""


class Student(object):
    count = 0

    # 实例方法
    def __init__(self, name):
        self.name = name
        Student.count += 1

    def del_count(self):
        Student.count -= 1

    # 类方法，可以修改和访问类属性，不能直接访问实例属性
    @classmethod
    def print_count(cls):
        return cls.count

    # 静态方法，不能访问类变量和实例变量
    @staticmethod
    def add_nums(self, x, y):
        # print(self.count)
        return x + y


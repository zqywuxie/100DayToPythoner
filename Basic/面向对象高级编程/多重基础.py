"""
@Project ：PythonLearnProject 
@File    ：多重基础.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 15:14 
@Description TODO 文件描述
"""


class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


# 设计通常称之为MixIn
# 需要其他功能，就进行多重继承
class Bird(Animal, Flyable):
    pass


# 各种动物:
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass

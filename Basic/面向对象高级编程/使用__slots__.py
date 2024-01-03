"""
@Project ：PythonLearnProject 
@File    ：使用__slots__.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 14:58 
@Description TODO 文件描述
"""


class Student(object):
    pass


s = Student()
s.name = 'ZQY'
print(s.name)


def set_age(self, age):
    self.age = age


from types import MethodType

# 为实例绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 其他实例不起作用
s2 = Student()
s2.set_age(123)
print(s2.age)

# 给全部实例都绑定方法，直接给class绑定方法
Student.set_age = set_age


# 如何限制实例的属性，不允许随便添加属性
class Animal(object):
    __slots__ = ('name', 'age')


animal = Animal()
animal.name = '123'
animal.score = 12  # Animal' object attribute 'score' is read-only
"""
使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用
对继承的子类是不起作用的：
"""


class Cat(Animal):
    pass


cat = Cat()
cat.score = 12  # 成功

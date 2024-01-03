"""
@Project ：PythonLearnProject 
@File    ：@property.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 15:05 
@Description TODO 文件描述
"""


# 对类属性赋值进行限制
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)  # ok!
s.get_score()


# 问题引出，怎样像普通变量一样进行提取和赋值


class Animal(object):
    @property
    def score(self):
        return self._score

    # 加@property本身创建了另一个装饰器
    # @名字.setter
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 不定义setter就是一个只读属性
    @property
    def age(self):
        return 2000 - self._score

    # 属性的方法名不要和实例变量重名
    # 会导致无限递归
    @property
    def birth(self):
        return self.birth


animal = Animal()
animal.score = 20
print(animal.score)

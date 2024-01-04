"""
@Project ：PythonLearnProject 
@File    ：序列化.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 23:28 
@Description TODO 文件描述
"""

# 字节序列化
import pickle

d = dict(name='Bob', age=20, score=88)

# 也可以通过dump保存到文件，load通过文件获得数据内容
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

# json序列化

import json

d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print('JSON Data is a str:', data)
reborn = json.loads(data)
print(reborn)


class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)


s = Student('Bob', 20, 88)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(std):
    return Student(name=std['name'], age=std['age'], score=std['score'])


# lambda表达式
# std_data = json.dumps(s, default=lambda obj: obj.__dict__)
std_data = json.dumps(s, default=student2dict)
print('Dump Student:', std_data)

# rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
rebuild = json.loads(std_data, object_hook=dict2student)
print(rebuild)

"""
@Project ：PythonLearnProject 
@File    ：iter.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 20:34 
@Description TODO 文件描述
"""


# import itertools
#
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))
#
# for key, group in itertools.groupby('AaaBBBCCAAA', lambda x: x.lower()):
#     print(key, list(group))


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('My name is %s' % self.name)


def myEnter(self):
    return next(self.__obj__)


def myExit(self, exc_type, exc_value, traceback):
    try:
        next(self.__obj__)
    except StopIteration as e:
        print('StopIteration', e.value)


def myInit(self, *args):
    self.__obj__ = self.__class__.__myFunc__(*args)


def my_contextlib(fun):
    mc = type('my_contextlib_class', (object,), dict(__init__=myInit, __enter__=myEnter, __exit__=myExit))
    mc.__myFunc__ = fun

    return mc


@my_contextlib
def create_user(name):
    q = Query(name)
    yield q
    return 'Done'


with create_user('ZQY') as user:
    print('Create_user call query', user)
    user.query()

"""
@Project ：PythonLearnProject 
@File    ：定制类.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 15:18 
@Description TODO 文件描述
"""
"""
类中有一些前后双下划线的变量或者函数名，起到特殊用途
__slots__,__len__()
我们可以定制类
"""


class Student(object):
    def __init__(self, name):
        self.name = name
        self.a = 1

    # 有点像Java的toString O.o
    def __str__(self):
        return 'Student object(name : %s)' % self.name

    # 返回一个迭代对象，实例本身就是迭代对象
    # 同时实现一个 __next__，for循环会自己调用进行下一个值
    def __iter__(self):
        return self

    def __next__(self):
        self.name += ':next()'
        self.a += 1
        if self.a == 4:
            raise StopIteration
        return self.name

    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

    # 对请求参数进行判断
    def __getattr__(self, item):
        if item == 'score':
            return 99
        if item == 'hah':
            return lambda x: x + 1

        # 默认返回None，自定义抛出错误
        raise AttributeError('\'Student\' object has no attribute %s' % item)
    # __str__


# print(Student('zqy'))  # Student object(name : zqy)

# __iter__
# for n in Student('demo'):
#     print(n)

# demo:next()
# demo:next():next()

# __getitem__
# s = Student('demo')
# print(s[5])

# 实现切片 要进行判断然后通过start和stop进行执行
# print(s[0:5])

# __getattr__
# s = Student('demo')
# print(s.hah(12))
# print(s.score)


# 链式调用，动态生成api接口路径
# class Chain(object):
#
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
#     # 直接对实例进行调用
#     def __call__(self, *args, **kwargs):
#         print('My path is %s' % self._path)


"""
# 你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用
能被调用的对象就是一个Callable对象
"""
# c = Chain().status.user.timeline.list
# c()  # My path is /status/user/timeline/list

# print(Chain().status.user.timeline.list)

"""
例题：GET /users/:user/repos
调用时，将:user换成实际用户名
Chain().users('michael').repos
"""


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self._path, item))

    def __str__(self):
        return self._path

    def __call__(self, name):
        return Chain('%s/%s' % (self._path, name))

    __repr__ = __str__


# users('zqy') 等于chain自己调用了一次
c = Chain().users('zqy')
print(c)

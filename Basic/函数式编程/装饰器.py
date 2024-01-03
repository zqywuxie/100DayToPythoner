"""
@Project ：PythonLearnProject 
@File    ：装饰器.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 10:22 
@Description TODO 文件描述
"""
import functools
import time


# wrapper名字自定义
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


def logWithArgs(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logWithArgs('execute')
def now():
    print(time.time())


@log
def local():
    print('123')


print(local.__name__)  # wrapper
print(now.__name__)  # wrapper

"""
所以要把原始函数的__name__等属性赋值到wrapper
否则一些依赖函数前面的代码会出问题
@functools.wraps(func)


"""

"""
把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)

3层嵌套的效果是这样的：
now = log('execute')(now)
"""

"""
@Project ：PythonLearnProject 
@File    ：文件操作.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 23:19 
@Description TODO 文件描述
"""
import os

print(os.name)
"""
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
使用os.path.join拼接字符串，因为不同操作系统斜杠方向不一样
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
"""

print(os.path.split('/user/demo.txt'))  # ('/user', 'demo.txt')
print(os.path.splitext('/user/demo.txt'))  # ('/user/demo', '.txt')

"""
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')

复制文件操作可以使用shutil库
"""
# 过滤文件
# listdir列出指定目录下的内容， isdir判断是否为目录
[x for x in os.listdir('.') if os.path.isdir(x)]
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

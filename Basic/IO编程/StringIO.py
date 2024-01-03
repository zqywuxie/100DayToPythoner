# """
# @Project ：PythonLearnProject
# @File    ：StringIO.py
# @IDE     ：PyCharm
# @Author  ：wuxie
# @Date    ：2024/1/3 23:12
# @Description TODO 文件描述
# """
#
from io import StringIO, BytesIO

f = StringIO()
f.write('hello world')
f.write('hello world \ ')
print(f.getvalue())

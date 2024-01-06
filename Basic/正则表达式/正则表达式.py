"""
@Project ：PythonLearnProject 
@File    ：正则表达式.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 18:39 
@Description TODO 文件描述
"""

import re

# pattern = '[0-9a-zA-Z_！！]+'
# print(re.match(pattern, '12345_！！'))
res = re.split(r'\s+', 'a b   c')
res1 = 'a b   c'.split(' ')
print(res)

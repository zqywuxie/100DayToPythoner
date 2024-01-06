"""
@Project ：PythonLearnProject 
@File    ：base64Decode.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 20:06 
@Description TODO 文件描述
"""
import base64


def safe_base64_decode(s):
    return base64.b64decode(s + ('===='[len(s) % 4:]))


# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

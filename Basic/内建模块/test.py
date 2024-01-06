# # """
# # @Project ：PythonLearnProject
# # @File    ：test.py
# # @IDE     ：PyCharm
# # @Author  ：wuxie
# # @Date    ：2024/1/4 19:50
# # @Description TODO 文件描述
# # """
# # #举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数
# #
# # from collections import ChainMap
# # import os, argparse
# #
# # defaults = {
# #     'color': 'red',
# #     'user': 'guest'
# # }
# #
# # parser = argparse.ArgumentParser()
# # parser.add_argument('-u', '--user')
# # parser.add_argument('-c', '--color')
# # namespace = parser.parse_args()
# # command_line_args = {k: v for k, v in vars(namespace).items() if v}
# #
# # # 组合成ChainMap:
# # combined = ChainMap(command_line_args, os.environ, defaults)
# #
# # # 打印参数:
# # print('color=%s' % combined['color'])
# # print('user=%s' % combined['user'])
#
#
# # backup.py
#
# import argparse
#
#
# def main():
#     # 定义一个ArgumentParser实例:
#     parser = argparse.ArgumentParser(
#         prog='backup',  # 程序名
#         description='Backup MySQL database.',  # 描述
#         epilog='Copyright(r), 2023'  # 说明信息
#     )
#     # 定义位置参数:
#     parser.add_argument('outfile')
#     # 定义关键字参数:
#     parser.add_argument('--host', default='localhost')
#     # 此参数必须为int类型:
#     parser.add_argument('--port', default='3306', type=int)
#     # 允许用户输入简写的-u:
#     parser.add_argument('-u', '--user', required=True)
#     parser.add_argument('-p', '--password', required=True)
#     parser.add_argument('--database', required=True)
#     # gz参数不跟参数值，因此指定action='store_true'，意思是出现-gz表示True:
#     parser.add_argument('-gz', '--gzcompress', action='store_true', required=False, help='Compress backup files by gz.')
#
#     # 解析参数:
#     args = parser.parse_args()
#
#     # 打印参数:
#     print('parsed args:')
#     print(f'outfile = {args.outfile}')
#     print(f'host = {args.host}')
#     print(f'port = {args.port}')
#     print(f'user = {args.user}')
#     print(f'password = {args.password}')
#     print(f'database = {args.database}')
#     print(f'gzcompress = {args.gzcompress}')
#     # print(f'gzcompress = {args.gz}')
#
#
# if __name__ == '__main__':
#     main()


import hmac, random


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

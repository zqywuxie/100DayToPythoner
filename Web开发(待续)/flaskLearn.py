"""
@Project ：PythonLearnProject 
@File    ：flaskLearn.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 22:06 
@Description TODO 文件描述
"""
import os

from flask import Flask, request, jsonify, redirect, url_for, make_response, abort, session, current_app, g
from utils import coverter

app = Flask(__name__)

"""
# 设置配置
# 对象加载
app.config.from_object()
#文件加载
app.config.from_pyfile()
#环境变量加载
app.config.from_envvar()
"""


# app.config.from_object(config.Config)
# app.config.from_pyfile('Config/config.ini')
# app.config.from_envvar('FLASKCONFIG')

@app.route('/hello')
def hello_world():
    print(f'{app.config}{app.config.get("DEBUG")}')


# <type:name>路径传参,可以指定参数类型
# methods = {'GET','POST'} 设置请求方式。默认GET方法
@app.route('/<int:user_id>', methods={'POST', 'GET'})
def index(user_id):
    print(type(user_id))
    return request.method


# 视图常见逻辑

@app.route('/json')
def returnJson():
    json_dict = {
        'user_id': 12,
        'user_name': 'zqy'
    }
    return jsonify(json_dict)


# 重定向某个网站，加上http协议，否则会被当作当前网站的某个子路径

@app.route('/demo')
def demo():
    return 'demo'


@app.route('/redirect')
def redirectR():
    # return redirect('https://www.baidu.com')
    return redirect(url_for('demo'))


# 自定义状态码

@app.route('/demo6')
def demo6():
    return 'ok', 555


# 自定义西相应信息

@app.route('/login')
def login():
    res = make_response('login fail')
    res.status_code = '999 login fail'
    res.headers['token'] = '1234'
    res.headers['city'] = 'chengdu'
    return res


app.url_map.converters['re'] = coverter.RegexConverter


@app.route('/login/<re("[1-9]{3}"):user_id>')
def rePattern(user_id):
    return f'user_id:{user_id}'


# 捕获异常,方法有个参数e
# @app.errorhandler(404)
# 也可以捕获指定错误
@app.errorhandler(ZeroDivisionError)
def abortD(e):
    # abort 主动抛出错误
    # abort(400)
    print(e)
    return '代码没有了'


"""====================请求hook"""


@app.before_request
def before_request():
    print('before')


@app.teardown_request
# 参数为服务器错误信息
def teardown(error):
    print('teardown')


# 参数为响应值
@app.after_request
def after_request(response):
    print('before_request')


"""================请求上下文"""
# 保存客户端和服务器交互的数据
# request/session
# request.args.get('user')
# session.get('name')

"""================应用上下文"""

# 保存flask运行中的一些配置信息
# 不是一直存在，request context中对app的代理，帮助request获得当前请求
# 生命周期跟随request
# current_app
# g.name = 'abc'

"""=================restful"""
# 每一个url表示一种资源，通过四个动词get，put，delete，post对资源进行操作

if __name__ == '__main__':
    app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql://root:mysql@127.0.0.1:3306/orm'
    app.run(host='0.0.0.0', port=5000, debug=True)

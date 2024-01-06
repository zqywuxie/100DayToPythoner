"""
@Project ：PythonLearnProject 
@File    ：05_cookie和session.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 19:03 
@Description TODO 文件描述
"""

# @Author  ：wuxie
# @Date    ：2024/1/5 18:58
# @Description TODO 文件描述

from flask import Flask, jsonify, make_response, request, session

app = Flask(__name__)


# cookie是基于客户端的，由服务端发送给客户端
# session是基于服务端的，客户端发起cookieId来找到对应的session


@app.route('/cookie')
def cookieDemo():
    resp = make_response()
    # 临时cookie，浏览器关闭就丢失
    resp.set_cookie("name", "age", 10)
    return resp
    # pass


@app.route('/get_cookie')
def getCookie():
    cookie = request.cookies.get('name')
    return cookie


@app.route('/de_cookie')
def de_cookie():
    resp = make_response()
    resp.delete_cookie('name')
    return resp


"""==========session"""
app.config["SECRET_KEY"] = "abcdefghijklm"


@app.route('/login')
def login():
    session["name"] = "zqy"
    session["mobile"] = "12323131231"
    return "login success"


@app.route('/index')
def index():
    name = session.get('name')
    return f"hello {name}"


if __name__ == '__main__':
    app.run()

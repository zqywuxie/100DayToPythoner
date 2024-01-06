"""
@Project ：PythonLearnProject 
@File    ：03_response.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 18:47 
@Description TODO 文件描述
"""

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/index')
def index():
    # return "index pass", 200, [("pp", "java")]
    # return "index pass", 200, {'name': 'zqy', 'age': 12}
    resp = make_response("page index")
    resp.status_code = 205
    resp.headers['pp'] = 'java'
    return resp


if __name__ == '__main__':
    app.run()

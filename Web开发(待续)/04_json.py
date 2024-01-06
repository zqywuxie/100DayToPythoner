"""
@Project ：PythonLearnProject 
@File    ：04_json.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 18:58 
@Description TODO 文件描述
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name': '123',
        'age': '234',
        'world': '1234',
    }
    # return jsonify(name='123', age='234')
    return jsonify(data)


if __name__ == '__main__':
    app.run()

"""
@Project ：PythonLearnProject 
@File    ：01_upload.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 18:32 
@Description TODO 文件描述
"""

from flask import Flask, request, abort, Response

app = Flask(__name__)


@app.route('/login', methods={'POST'})
def login():
    name = request.form.get('name')
    print(name)
    if name != 'zqy':
        print('123')
        # abort(404)
        resp = Response('login failed')
        abort(404)
    return 'login success'




if __name__ == '__main__':
    app.run()

"""
@Project ：PythonLearnProject 
@File    ：07_表单.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 19:42 
@Description TODO 文件描述
"""
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/regx', methods=["POST","GET"])
def regx():
    text = ""
    if request.form.get('text'):
        text = request.form.get('text')
    return render_template('login.html', text=text)


if __name__ == '__main__':
    app.run()

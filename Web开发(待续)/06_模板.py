"""
@Project ：PythonLearnProject 
@File    ：06_模板.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 19:24 
@Description TODO 文件描述
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        "name": "zqy",
        "age": 22,
        "mobile": 15182852522,
        "my_list": [1, 2, 2, 3, 5],
        "my_dict": {"city": "dazhou"}
    }
    return render_template('index.html', **data)


# 自定义过滤器
def list_2_ste(li):
    return li[::2]


# 然后进行模板过滤器的注册
app.add_template_filter(list_2_ste, 'li2')

if __name__ == '__main__':
    app.run()

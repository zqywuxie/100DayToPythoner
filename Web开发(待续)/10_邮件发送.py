"""
@Project ：PythonLearnProject 
@File    ：10_邮件发送.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/6 18:19 
@Description TODO 文件描述
"""
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.163.com'  # 配置邮箱
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = '15182852522@163.com'
app.config['MAIL_PASSWORD'] = 'RLUJLXWCALLGDXWF'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)  # 创建Mail类实例


@app.route("/")
def index():
    msg = Message('Hello', sender='15182852522@163.com', recipients=['573905257@qq.com'])
    msg.body = "Hello World"
    mail.send(msg)
    return "Sented"


if __name__ == '__main__':
    app.run(debug=True)

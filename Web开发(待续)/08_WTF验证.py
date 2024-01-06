"""
@Project ：PythonLearnProject 
@File    ：08_WTF验证.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/5 19:49 
@Description TODO 文件描述
"""
from flask import Flask, redirect, url_for, render_template, request, session
# pip install flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'abcdefg'


# 定义一个表单的模型类
class RegisterForm(FlaskForm):
    user_name = StringField(label=u'用户名', validators=[DataRequired(u"用户名不能为空")])
    password = PasswordField(label=u'密码', validators=[DataRequired(u'密码不能为空')])
    password2 = PasswordField(label=u'验证密码',
                              validators=[DataRequired(u'密码不能为空'), EqualTo('password', u'两次密码要一致')])
    submit = SubmitField(label=u'提交', )


@app.route('/regis', methods=['POST', 'GET'])
def regis():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.user_name.data
        password = form.password.data
        checkpw = form.password2.data
        print(name, password, checkpw)
        session["username"] = name
        #  post请求后跳转，前台需要添加form.csrf_token
        # 确保是在服务端返回的表单中的数据
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/index')
def index():
    u_name = session.get('username')
    return f'hello {u_name}'


@app.route('/hong')
def hong():
    return render_template('hong.html')


if __name__ == '__main__':
    app.run()

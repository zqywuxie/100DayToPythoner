"""
@Project ：PythonLearnProject 
@File    ：bookstore.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/6 16:45 
@Description TODO 文件描述
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from flask_script import Manager
# 出现no module name mysqldb
# 安装mysqlclient/pymysql(安了也有问题)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired

# 安装flask_sqlalchemy_db
# 要安装Flask—sqlalchemy?

app = Flask(__name__)


class Config(object):
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:wszqy123.@127.0.0.1:3306/sqlal"

    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)
app.config["SECRET_KEY"] = "abcdefghijklmnopqrstuvwxyz"

# 创建工具对象

db = SQLAlchemy(app)

manager = Manager(app)

migrate = Migrate(app, db)


class Author(db.Model):
    __tablename__ = "tb_author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    # backref提供Book对author的引用
    # books是author对book的引用
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    __tablename__ = "tb_books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    author_id = db.Column(db.Integer, ForeignKey("tb_author.id"))


class AuthorBookForm(FlaskForm):
    author_name = StringField(label=u"作者", validators=[DataRequired(u"请填写作者名")])
    book_name = StringField(label=u"图书", validators=[DataRequired(u"请填写书名")])
    submit = SubmitField(label="保存书籍")


@app.route('/index', methods=["POST", "GET"])
def index():
    form = AuthorBookForm()
    if form.validate_on_submit():
        author_name = form.author_name.data
        book_name = form.book_name.data
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()
    authors = db.session.query(Author).all()
    print(authors)
    return render_template("bookstore.html", authors=authors, form=form)


# /delete?deleteid=xxx  通过request.args.get获得参数
@app.route('/delete', methods={"POST", "GET"})
def delete():
    bookid = request.args.get('bookid')
    book = db.session.query(Book).get(bookid)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("index"))


# <type:name>路径传参,可以指定参数类型
# methods = {'GET','POST'} 设置请求方式。默认GET方法
@app.route('/<int:user_id>', methods={'POST', 'GET'})
def routeDemo(user_id):
    print(type(user_id))
    return request.method


if __name__ == '__main__':
    app.run()

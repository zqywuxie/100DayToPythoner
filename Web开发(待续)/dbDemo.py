"""
@Project ：PythonLearnProject 
@File    ：dbDemo.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/6 14:50 
@Description TODO 文件描述
"""

from flask import Flask, session
# 安装flask_sqlalchemy_db
# 要安装Flask—sqlalchemy?

# 出现no module name mysqldb
# 安装mysqlclient/pymysql(安了也有问题)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, create_engine, and_, or_, not_, func
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


class Config(object):
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:wszqy123.@127.0.0.1:3306/sqlal"

    # 自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


app.config.from_object(Config)

# 创建工具对象

db = SQLAlchemy(app)


# 创建模型
class Role(db.Model):
    __tablename__ = "tb1_roles"

    # 数据库表指定名字
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    user = db.relationship("User", backref="role")

    def __repr__(self):
        # 直观表示对象
        return f"Role Object:name = {self.name}"


class User(db.Model):
    __tablename__ = "tb1_users"
    # 数据库表指定名字
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    phone = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    # 设置外键
    role_id = db.Column(db.Integer, ForeignKey("tb1_roles.id"))

    def __repr__(self):
        # 直观表示对象
        return f"User Object:name = {self.name}"


if __name__ == '__main__':
    # 直接删除和创建会有问题，需要结合上下文进行
    # db.create_all()
    # app.run()
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()

    # 创建引擎和会话
    # engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    # Session = sessionmaker(bind=engine)
    # session = Session()

    role = Role(name="test09123")

    # with app.app_context():
    #     db.session.add(role)
    #     db.session.commit()
    #
    #     user = User(name="zq0y", phone="1203467", password="123123123", role_id=role.id)
    #     user1 = User(name="zq0y13", phone="102341467", password="1231243123", role_id=role.id)
    #     db.session.add_all([user, user1])
    #     db.session.commit()
    with app.app_context():
        all = db.session.query(Role).all()
        # all = session.query(Role).all()
        # print(all[0].name)

        # filter_by 接受关键字参数 **kwargs
        # filter = db.session.query(User.name).filter_by(name="zqy").all()

        # filter 进行参数比较
        filter = db.session.query(User.name).filter(User.name == "zqy").all()
        # 模糊查询
        mohu = db.session.query(User.name).filter(User.name.like('%zqy%')).all()

        # 逻辑操作 not_,or_,and_
        andRes = db.session.query(User.name).filter(not_(User.name.like('%zqy%'))).all()

        offsetRes = db.session.query(User.name).offset(3).limit(2).all()
        total = db.session.query(User.name).all()
        # asc升序 desc降序
        sorted = db.session.query(User.name).order_by(User.role_id.asc()).all()
        # print(offsetRes)

        # func 数据库里面的函数操作
        groups = db.session.query(User.role_id, func.count(User.role_id)).group_by(User.role_id).all()

        # 根据主键获得信息
        # first = db.session.query(User).get(4)
        users = db.session.query(Role).get(3).user
        print(users[0].name)

        # db.session.query(User).filter(User.name == 'zqy').update({"phone": '1212', "password": '234'})
        # db.session.commit()

        db.session.query(User).filter(User.name.like('%zq0%')).delete()
        db.session.commit()

        # print(total)
        # print(sorted)
        # print(groups)

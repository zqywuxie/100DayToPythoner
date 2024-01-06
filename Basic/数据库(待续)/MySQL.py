"""
@Project ：PythonLearnProject 
@File    ：MySQL.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/4 21:57 
@Description TODO 文件描述
"""
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='wszqy123.',
    port=3306,
    database='gorm'
)
# 创建游标，查询数据以元组形式返回
# cursor = conn.cursor()

# 创建游标，查询数据以字典形式返回
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = 'select * from user limit 10'
try:
    cursor.execute(sql)
    # result = cursor.fetchall()  # 返回所有数据
    # result = cursor.fetchone()  # 返回一行数据
    result = cursor.fetchmany(2)  # fetchmany(size) 获取查询结果集中指定数量的记录，size默认为1
    print(result)
except Exception as e:
    conn.rollback()
    print(e)
finally:
    cursor.close()
    conn.close()


# 元组、列表形式传参
sql = 'insert into player_info_test(PERSON_ID,PERSON_NAME,AGE) VALUES(%s, %s, %s)'
try:
    cursor.execute(sql, ("999999", "kenny", 28))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
finally:
    cursor.close()
    conn.close()


# 字典形式传参
sql = 'insert into player_info_test(PERSON_ID,PERSON_NAME,AGE) VALUES(%(person_id)s, %(person_name)s, %(age)s)'
try:
    cursor.execute(sql, {"person_id": "999998", "person_name": "kenny", "age": 28})
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
finally:
    cursor.close()
    conn.close()
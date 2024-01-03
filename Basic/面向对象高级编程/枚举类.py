"""
@Project ：PythonLearnProject 
@File    ：枚举类.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 16:04 
@Description TODO 文件描述
"""

from enum import Enum, unique

# 参数1：枚举的name
# 参数2：枚举的各个内容，数字从1开始
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)


# 方便控制枚举，可以自定义枚举类
# unique检查没有重复值
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Fri.value)  # 5
print(Weekday['Fri'])  # Weekday.Fri
print(Weekday(5))  # Weekday.Fri

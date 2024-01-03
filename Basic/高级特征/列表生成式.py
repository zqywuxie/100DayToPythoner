"""
@Project ：PythonLearnProject 
@File    ：列表生成式.py
@IDE     ：PyCharm 
@Author  ：wuxie
@Date    ：2024/1/3 8:56 
@Description TODO 文件描述
"""

list = [x * x for x in range(1, 12)]
list2 = [m + n for m in 'ABC' for n in 'BCD']
print(list2)

# dict的items 同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# if...else
# 输出偶数
print([x for x in range(1, 11) if x % 2 == 0])

# 不能在if后面直接加else
# 因为后面的if起到一个筛选作用，而不是判断
# print([x for x in range(1, 11) if x % 2 == 0 else 0])

# 也不能直接把if写在前面
# 因为前面是一个表达式，需要得出一个值，而只是判断
# 所以将if..else写在前面
# print([x if x % 2 == 0 for x in range(1, 11)])

# print([x if x % 2 == 0 else 3 for x in range(1, 11)])

l2 = [1, "abv", True]
print([x.upper() for x in l2 if isinstance(x, str)])

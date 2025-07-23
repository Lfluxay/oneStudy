"""
列表推导式：可以快速生成一个列表
li = [i for i in xxx]
"""

# 需求：生成一个列表1—20
# for循环语法
li = []
for i in range(1,21):
    if i == 0:
        continue
    d = "{}".format(i)
    li.append(d)
print(li)

# 列表推导式
# li2 = ['page{}'.format(i) for i in range(21)]
# print(li2)

# 元组中的数据处理转为列表
# tu = (11, 22, 33, 44, 55, 66, 77)
# li = [i+1 for i in tu]
# print(li)


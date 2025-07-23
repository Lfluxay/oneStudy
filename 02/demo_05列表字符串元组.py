"""
字符串、列表、元素：是序列类型
1、序列的共同特征
    都有索引值：内部的元素都是有序的
    支持切片操作
都可以通过len()去获取元素的个数、数据长度

数据类型的相互转换：
数值：
    整数
    浮点数
    布尔值
序列：
    字符串
    列表
    元组


"""
# 数字转换字符串
# n1 = 99
# n2 = 99.00
# print(type(n1), type(n2))
#
# n3 = str(n1)
# n4 = str(n2)
# print(type(n3), type(n4))
#
# 字符串转数字
s1 = "1234"
s2 = "99.91"
print(type(s1), type(s2))

s3 = int(s1)
s4 = float(s2)
print(type(s3), type(s4))
#
#
# 列表和元组之间的转换
# 列表转元组
l1 = ["jack", 12, "man"]
t1 = tuple(l1)
print(type(l1))
print(t1,type(t1))

# 元组转列表
t = ("jack", 12, "man")
l = list(t)
print(type(t))
print(l, type(l))

# 字符串和列表之的转换
l1 = [11, 22, 33, 44, 55]
s = str(l1)
print(s)
print(s, type(s))


# 需求将如下列表转为一个列表
s = '[11,22,33,44,55]'
t = '(11,22,33,44,55)'
li = list(s)
print(li)


# 内置函数eval，去除字符串两边的引号
li2 = eval(s)
s1 = eval(t)
print(s1,type(s1))
print(li2,type(li2))

# 快速定义元组
tu = 11, 22, 33
print(tu, type(tu))

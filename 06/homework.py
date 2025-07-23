"""
函数的参数定义有哪几种形式？
    必需，缺省，不定长

函数参数的调用有哪几种形式？
    位置传参，关键字传参
"""


"""
写一个可以打印任意比例正方形的函数
"""
# def taget(a):
#     for i in range(a):
#         for i in range(a):
#             print(" * ",end='')
#         print()
# taget(6)


"""
完善如下的计算器函数的功能代码：
def func(a,b,method):
    参数a:数字
    参数b:数字
    参数method：计算方法：可以传"+-*/"
"""
# def func(a,b,method):
#     if method == "+":
#         print("a+b:",a+b)
#     elif method == "-":
#         print("a-b:",a-b)
#     elif method == "*":
#         print("a*b:",a*b)
#     elif method == "/":
#         print("a/b:",a/b)
# func(12,28,"*")


"""
定义一个可以完成任意个数字相加的函数(支持关键字传参和位置传参),并打印相加结果。
要求:调用函数传入1个数字,则打印这个数
    如:func(1)---------打印1
调用函数传入2个数字,返回值为2个数相加的结果
    如:func(11,22)-------打印33
调用函数传入3个数字,返回值为3个数相加的结果
    如:func(11,22,33,)--->打印66
调用函数传入n个数字,返回值为n个数相加的结果
    如:func(1,2,3,4,5)--->打印15
"""
# def add(*args,**kwargs):
#     print(sum(args,kwargs))
# add(1,2,3)


# 方法2
def func(*args, **kwargs):
    s = 0
    for i in args:
        s += i
    for j in kwargs.values():
        s += j
        """
     for j in kwargs:
        s += kwargs[j]
        """
    print(s)
func(1, 2, 3, c=12, b=99)


"""
定义一个函数：要求使用下面方式取调用不报错
li = [11,22,33]
dic = {"a":11,"b":22,"c":33,"d":44}

func(*li)
func(**dic)
"""
# li = [11, 22, 33]
# dic = {"a": 11, "b": 22, "c": 33, "d": 44}
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# func(**dic)
# func(*li)




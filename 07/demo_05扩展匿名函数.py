"""
匿名函数：
    适用于函数内部代码非常简单的函数

    语法：
        lambda 参数：返回值



"""

def func(x):
    return x * 2

res = func(10)
print(res)

# 接受一个参数的匿名函数
func1 = lambda x: 2 * x
res2 = func1(10)
print(res2)

# 接收两个参数的匿名函数
func2  = lambda x, y: x + y
res3 = func2(999,111)
print(res3)


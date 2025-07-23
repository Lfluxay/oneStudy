"""
分类：
    调用的时候，传参的类型
    1.位置参数

    2.指定参数名传参

    注意点：传参顺序以及位置



"""
# 传参
# def add(a,b):
#     c = a + b
#     print(c)
#
# add(11,22)
#
# add(a=59,b=33)

def num(a,b,c,d):
    print("1:", a)
    print("2:", b)
    print("3:", c)
    print("4:", d)

# 混合使用，位置写前面，指定参数写后面
num(2,3,c=9,d=9)


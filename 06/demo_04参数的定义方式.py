"""
参数定义的方式;
    必需参数-必备
        def func(a,b):

    缺省参数-默认
        def func(c=xx,b=xx):

    可变参数-不定长
    *args:只能通过位置传参，以元组形式保存
    **kwargs:只能通过关键字参数形式传入，字典形式保存


# 注意点：必需参数写前面，默认参数写后面

"""
# 必需参数,定义几个传入几个
# def add(a,b,c):
#     d = a+b+c
#     print(d)
# add(1,2,3)

# 缺省参数,定义之后，调用时可传可不传
# def add(a,b,c=99):
#     d = a+b+c
#     print(d)
# add(1,2,11)
# add(1,3)

# 可变参数，调用的时候，可传0个或多个参数
# def add(*args):
#     print(args)
# add(11,22,33,4455)

# def add(**kwargs):
#     print(kwargs)
#
# add(a=11,b=222)

# 需求,定义一个可以接收任意个参数的函数，同时支持位置传参和关键字传参
# def add(*args,**kwargs):
#     print(args,kwargs)
#
# add(1,2,3,b=123)


# 三种形式传参方式函数定义
def add(a,b,c=99,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

add(1,2,44,444,o=12312312)

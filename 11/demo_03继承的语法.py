"""
方式1：
    class 类名:
        pass

方式2：
    class 类名(object):
        pass

上述两种类定义的方法，都是默认继承object


object:
    所有类的顶级父类(基类)

"""

class Demo(object):
    pass

class Demo2(Demo):
    pass


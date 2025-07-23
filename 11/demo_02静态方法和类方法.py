"""
实例方法：
    只能通过对象调用
    参数1：self
        代表对象本身
    适用场景:
        方法内部如果要使用对象的属性或方法，就要定义为对象方法

静态方法定义：要使用@staticmethod声明

    静态方法：
        无固定参数

        可以通过类调用，也可以通过对象调用
        适用场景：
            方法内部，既不需要类属性方法也不需要使用对象属性和方法，适合定义为静态方法


类方法定义：要使用@classmethod声明

    类方法：
        参数1：cls
            代表类本身
        可以通过类调用，也可以通过对象调用
        适用场景：
            方法内部只使用类属性或者类方法，不需要使用对象属性和方法,适合定义为类方法

"""
# class MyClass:
#
#     def info(self):
#         print("____info_____实例方法")
#
#     @classmethod
#     def info_cls(cls):
#         print(cls)
#         print("____info_____类方法")
#
#     @classmethod
#     def info_static(cls):
#         print("____info_____静态方法")
#
# # 通过类调用
# MyClass.info_cls()
# # 通过对象调用
# cat = MyClass()
# cat.info_cls()


class MyTest:
    attr = 100

    def __init__(self, name):
        self.name = name

    def func1(self):
        print(self.name)

    @classmethod
    def func2(cls):
        print(cls.attr)

    @staticmethod
    def func3():
        print("静态方法")

test = MyTest
test.func3()
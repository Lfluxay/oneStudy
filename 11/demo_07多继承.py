
"""
多继承
    同时继承多个父类

    若父类同名的方法：
        只会调用其中一个父类的方法

"""
class BaseA:
    A = 100
    def func(self):
        print("---A---")

class BaseB:
    B = 200
    def func1(self):
        print("---B---")

class MyClass(BaseA,BaseB):
    pass

m = MyClass()
m.func1()
m.func()
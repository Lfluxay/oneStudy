"""
私有属性：
    仅供内部使用，不要在外部调用
    _开头：
        表示这是一个私有属性，没有真正私有化，外部依旧可以调用
    __开头
        表示这是一个私有属性，真正私有化，类外部不可调用


私有方法：
    _开头：
        表示这是一个私有方法，没有真正私有化，外部依旧可以调用
    __开头
        表示这是一个私有方法，真正私有化，类外部不可调用

"""


class MyClass:
    _attr = 100
    __name = "jack"

    def __get_info(self):
        print("___get_info")

    def _get_name(self):
        print("___get_info")

    def func(self):
        print(self.__name)


b = MyClass()
# 没有完全私有化，类外部可调用-------
# print(b._attr)

# 完全私有化，类外部不可调用-------
# print(b.__name)

# 内部函数调用，类外部调用函数才能进行调用
b.func()


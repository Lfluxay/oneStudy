"""

"""

# class Person():
#     pass
#
# jack = Person()
# jack.name = "杰克"
# jack.age = 18
# jack.high = 187
# jack.gender = "男"
#
# rose = Person()
# rose.name = "鲍博"
# rose.age = 21
# rose.high = 174
# rose.gender = "男"



# __init__方法的使用，特殊方法，不需要手动调用，特定情况下自动调用
# 在类创建对象的时候调用的方法

class Person:
    attr = "类属性"
    def __init__(self, name, age, sex):
        # 在创建对象的时候，给对象设置对象属性
        self.name = name
        self.age = age
        self.sex = sex
        print("这个是初始化方法")

    # 需要手动调用
    def func(self):
        self.high = 170

jack = Person("admin",19,"man")
rose = Person("test",17,"women")

# 需要手动调用
jack.func()
print(jack.high)

# 自动调用
print(jack.name, jack.age, jack.sex)


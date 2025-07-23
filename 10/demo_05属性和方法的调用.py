"""
类属性的调用
    可以通过类去调用   ----- 类.属性名
    也可以通过对象调用    -----对象.属性名

实例属性的调用:
    只能通过对象去调用自己的属性

方法的调用：
    不能直接用类调用（因为没有对象）
    只能通过对象去调用

方法的分类：
    方法中第一个参数是self的方法，叫做实例（对象）方法

类方法：
静态方法：
"""

class Cat:
    leg = 4
    tail = 1
    eye = 2

    def catch(self):
        print("catch 3")

    def skills(self):
        print("jump tree")

# 通过类属性创建对象
coffee = Cat()
single = Cat()

# 通过类实例化对象
coffee.name = "jack"
single.name = "rose"

# 类属性的调用----------
print(Cat.leg)
print(coffee.leg)

# 实例属性的调用---------
# print(Cat.name)   类调用不了
# print(coffee.name)


# 方法的调用-----------
# Cat.catch() # 不能直接类调用
coffee.catch() # 只能通过对象去调用
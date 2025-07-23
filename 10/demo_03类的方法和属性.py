"""

特征：
    属性
行为：
    方法

类的方法和属性：
    属性：
        类属性：这类事物都具备的属性，且属性值都是一样的，定义位类属性
                类属性是所有的对象共有的

                类属性的定义：
                    直接定义在类里面的变量
                    类名.属性名 = 属性值

        对象（实例）属性：对象有独有的，对象自己的特征
                实例属性的定义：
                    对象.属性名 = 属性值

    方法：
        定义在类里面的函数叫做方法

        方法中的参数除了self之外，其他参数的传递和函数是一样的

        方法中也是使用return返回数据的

        默认参数self的意思：表示对象本身




"""

class Cat:
    leg = 4
    tail = 1
    eye = 2

    def catch(self):
        print("catch mouse")

    def skills(self):
        print("jumping tree")

# 类属性
coffee = Cat()

# 通过类实例化对象
coffee.name = "jack"
coffee.age = "18-mon"

# 通过对象调用方法
coffee.catch()

single = Cat()
single.name = "rose"
single.age = "12-mon"



# ================方法怎么使用====================
s = "abc"
res = s.replace("a","e")
print(res)

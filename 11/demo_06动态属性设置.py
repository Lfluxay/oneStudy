"""
    # 动态属性设置：
    setattr()
        括号内3个参数
        参数1:对象（类）
        参数2:属性名
        参数3:属性值

    # 动态获取属性
    getattr()
        括号内2个参数
        参数1:对象（类）
        参数2:属性名
        参数3：非必传参数，设置一个属性不存在的默认返回值，若不传，属性不存在会报错

    # 动态删除属性
    delattr()
        括号内2个参数
        参数1:对象（类）
        参数2:属性名

    # 判断属性是否存在
    hasattr()
        括号内2个参数
        参数1:对象（类）
        参数2:属性名



"""
# -----------------setattr()--------------------------
# class MyClass:
#     attr = 100

# 查看所有属性
# print(MyClass.__dict__)

# 在代码执行的过程中给类添加属性
# 方式1：通过类名
# MyClass.name = "jack"
# print(MyClass.name)

# 引入
# key = "name"
# value = "jack"
# setattr(MyClass,key,value)

# 需求：把字典中的键值对设置为类的属性和属性值
# data = {"name":"jack", "age":18, "gender":"man"}
# for k,v in data.items():
#     setattr(MyClass,k,v)
# print(MyClass.__dict__)

# 需求：给对象设置属性名和属性值
# 对类进行实例化
# res = MyClass()
# # 需求内容设置
# data = {"name":"jack", "age":18, "gender":"man"}
# # 遍历字典的键值，分别设置键为属性名，设置值为属性值
# for k,v in data.items():
#     setattr(res,k,v)
# print(res.__dict__)
# # 因为是动态的属性，所以标黄
# print(res.name)
# print(res.age)
# print(res.gender)


# --------------getattr()-----------------------------
# class MyClass:
#     attr = 100
#     name = "jack"
#     age = 18
#
# # 使用法
# key = input("请输入要获取的属性值：")
# res = getattr(MyClass,key,None)
# print(res)


# --------------delattr()-----------------------------

# 关键字，del，作用删除
# class MyClass:
#     attr = 100
#     name = "jack"
#     age = 18
#
# # 使用法
# key = input("请输入要删除的属性值：")
# delattr(MyClass, key)
# print(MyClass.__dict__)


# --------------hasattr()-----------------------------
class MyClass:
    attr = 100
    name = "jack"
    age = 18

# 判断是否存在一个属性，传统方法
try:
    res = MyClass.attr
except:
    print("no")
else:
    print(res,"have")

# 新方法
key = input("请输入要判断的属性值：")
res = hasattr(MyClass, key)
print(res)

if hasattr(MyClass, "nam1"):
    print("have")
else:
    setattr(MyClass, "money", 110)
print(MyClass.__dict__)
"""
三种定义：
    1.dic = {"name": "jack","age": 18,"gender": "男"}

    2.dict

    3.dict赋值

"""
# 直接定义
dic = {"name": "jack","age": 18,"gender": "男"}

# dict函数
dic2 = dict([("name","jack"),("age",18)])
print(dic2)

# dict函数方法2
dic3 = dict(name="rose",
            age=18,
            gender="男")
print(dic3)
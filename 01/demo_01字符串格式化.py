
# name = input("请输入name：")
# money = input("请输入money：")

"""
# 字符串拼接
des = "今收到" + name + "交学费，" + money +"元"
print(des)
"""

"""
# format传参
des = "今收到{}，交学费{}元".format(name,money)
print(des)
"""

"""
# %占位符,%d-整数占位符,%f-浮点数占位符(限数值)，%s-字符串占位符（任意类型）
des = "今收到%s，交学费%s元"%(name,money)
print(des)
"""

# 字符串，f表达式
"""
name = "jack"
age = 15
des = f'收到{name},年龄{age}'
print(des)
"""
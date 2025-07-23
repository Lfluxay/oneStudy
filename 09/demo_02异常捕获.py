"""
try:
    有可能出错的代码
except:
    当try里面的代码执行出错时，执行expect里面的代码，可以在这里对异常进行处理
"""
# 捕获全部异常
# try:
#     num = float(input("输入一个数字："))
# except Exception as e:
#     # 此处可以对异常进行处理
#     # print("当try执行出错，执行这里")
#     print("输入有误")
#     num = 0
#     # 输出错误信息
#     print('错误信息',e)


# 捕获指定异常
# dic = {"a":11}
# # print(dic["b"])
# try:
#     print('----1-----')
#     print(name)
#     # 有多行代码，一行报错，后面不执行
#     print('----1-----')
#     print(dic["b"])
# except Exception as e:
#     print(e)

# 捕获多个异常
dic = {"a":11}
# print(dic["b"])
try:
    print(name)
    print(dic["b"])
except Exception as e:
    print("nameerror",e)
except KeyError as a:
    print("keyerror",a)
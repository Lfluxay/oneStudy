"""
try:
    有可能出错的代码(会检测代码是否出错)
except:
    当try里面的代码执行出错时，执行expect里面的代码，可以在这里对异常进行处理
else:
    try中的代码没有执行出错，则执行这里的
finally:
    无论try是否报错,异常是否捕获到，始终都会执行此部分的代码
"""
# data.txt读取内容，然后在写入Python你好
#
# try:
#     with open(file="data.txt",mode="r",encoding="utf-8") as f:
#         res = f.read()
#         print(res)
# except:
#     print("not find data.txt")
# else:
#     print(res)
#
# with open(file="data.txt",mode="w",encoding="utf-8") as f:
#     f.write("hello,套你猴子")


# 完整语法流程
# name = "exe"
# try:
#     print(name)
# except:
#     print("not find")
# else:
#     print("find")
# finally:
#     print("finally run")


# 拓展
# 需求 注册账号

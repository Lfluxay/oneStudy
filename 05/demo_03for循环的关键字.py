"""
continue:
    结束本次循环,开启下一次

break:
    强制终止循环


for x in xxx:
    # 循环体
else:
    # 循环正常结束执行

"""
# for i in range(9):
#     if i == 5:
#         continue
#     print(i)

# for i in range(9):
#     if i == 5:
#         break
#     print(i)

# 正常结束执行else
for i in range(9):
    print("--{}-".format(i))
else:
    print("xxx")


# 非正常结束，不执行else
for i in range(9):
    print("--{}-".format(i))
    if i == 5:
        break
else:
    print("xxx")


# 判断输入的数据是否存在
li = [
    {"name":"jack","pwd":"123456"},
    {"name":"rose","pwd":"111111"},
    {"name":"luck","pwd":"123123"}
]
name = input("请输入用户名：")
pwd = int(input("请输入密码："))
for i in li:
    if i["name"] == name and i["pwd"] == pwd:
        print("true")
        break
else:
    print("false")
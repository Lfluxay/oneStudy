"""
代码执行的顺序：从上往下
分支：根据不同的条件，执行不同的代码
循环：特定的代码重复执行
----------------------------
    if 条件:
        # 成立执行的代码
    else:
        # 不成立执行的代码
----------------------------
    if 条件:
        # 成立执行的代码
    elif:
        # 成立执行的代码
    else:
        # 不成立执行的代码

"""
# grant = int(input("请输入考试的分数："))
# if grant >= 60:
#     print("及格")
# else:
#     print("不及格")


grant = int(input("请输入考试的分数："))
if grant <= 59 and grant >= 0:
    print("d")
elif grant <= 75 and grant >= 0:
    print("c")
elif grant <= 85 and grant >= 0:
    print("b")
elif grant <= 95 and grant >= 0:
    print("a")
elif grant <= 100 and grant >= 0:
    print("s")
else:
    print("输入有误")
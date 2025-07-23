"""
嵌套使用：

 # 需求1
* * * *
* * * *
* * * *
* * * *

"""
# for i in range(4):
#     print("* * * *")

# for i in range(4):
#     for j in range(4):
#         print("* ",end = '')
#     print()

# 正三角
# for i in range(4):
#     for j in range(4-i):
#         print("* ",end = '')
#     print()
#
# # 倒三角
# for i in range(4):
#     for j in range(i+1):
#         print("* ",end = '')
#     print()


# 99乘法表
for i in range(10):
    for j in range(i+1):
        if j == 0:
            continue
        print("{}x{}={} ".format(i,j,i*j),end = '')
    print()



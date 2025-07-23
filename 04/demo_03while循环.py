"""
while 条件:
    # 条件成立，循环执行代码1
    。。。。

    break:终止循环

    continue：中止当前本轮循环，回到开始


"""
# 循环打印
# a = 1
# while a <= 100:
#   print("hello = {}".format(a))
#   a = a + 1
# print("___end____")

a = 0
while a < 15:
    a += 1
    if a == 8:
        continue
    print("hello = {}".format(a))
print("----end----")



"""
字典遍历：{"a":1,"b":22,"c":3,"d":4,"e":5}
修改字典中的键值对，新的值乘10
"""
# dic = {"a":1,"b":22,"c":3,"d":4,"e":5}
# for i in dic:
#     dic[i] = dic[i]*10
# print(dic)


"""
请生成如下的列表:["data5","data10","data15",..."data95"]
"""
# li1 = ["data{}".format(i) for i in range(5,96,5)]
# print(li1)

li = []
for i in range(5,96):
    if i % 5 == 0:
        #if i == 0:
           # continue
        d = "data{}".format(i)
        li.append(d)
        continue
print(li)



"""
运行程序，提示用户依次输入三个数x,y,z，请把这三个数从小到大输出
"""
# x = int(input("请输入一个数："))
# y = int(input("请输入一个数："))
# z = int(input("请输入一个数："))
# num = [x, y, z]
# num.sort()
# for i in num:
#     print(i)



"""
输出99乘法表
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         # if j == 0:
#         #     continue
#         print("{}*{}={:<4} ".format(i,j,i*j),end='')
#     print()

"""
有1 2 3 4 四个数字，请通过代码计算能实现多少不重复的3位数,并打印
"""
li = [1,2,3,4]
count = 0
for a in li:
    for b in li:
        for c in li:
            if a != b and a != c and b != c:
                print("{},{},{}".format(a,b,c))
                count += 1
print("{}".format(count))
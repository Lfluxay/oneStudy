# 1.现在有一个列表 li = [1,2,3,4,5]
#     添加和修改操作，成为li1 = [0,1,2,3,66,5,11,22,33]
#     进行升序操作
#     复制列表进行降序操作
# li = [1,2,3,4,5]
# li.insert(0,0)
# li.extend((11,22,33))
# li[4] = 44
# print(li)
#
# li.sort(reverse=False)
# print(li)
#
# li_01 = li.copy()
# li_01.sort(reverse=True)
# print(li_01)

# 2.定义空列表，提示输入姓名、年龄、身高，输入之后
#     输出内容，按照格式
#     输入信息保存至列表，打印
# user = []
# name = input("请输入姓名：")
# age = input("请输入年龄：")
# high = input("请输入身高:")
# print('用户的身高为：{}，年龄为：{}，身高为{},请核对数据'.format(name,age,high))
# user.extend([name,age,high])
# print(user)


# 3.字符串反转 hello转为olleh
#
# s = 'hello'
# print(s[::-1])
#
# str1 = 'hello xiao mi'
# data = str1.split(' ')
# print(data)
# data.reverse()
# res = ' '.join(data)
# print(res)


# 4.列表和元组的切片练习
#     li = [1,2,3,4,5,6,7,8,9],切出结果[3,6,9]
#     tu = ('java','c++','python','c','php','c#'),切出('java','php')

# li = [1,2,3,4,5,6,7,8,9]
# print(li[2::3])
#
# tu = ('java','c++','python','c','php','c#')
# print(tu[0::4])

# 5.提示输入1-7,根据输入数字判断为星期几
# data = ["周一","周二","周三","周四","周五","周六","周天"]
# print(data[0])
# num = int(input("请输入1-7之间的一个数字："))-1
# des = "今天是{}".format(data[num])
# print(des)
data = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]
num = int(input("请输入1-7中的一个数:"))
res = "今天是{}".format(data[num-1])
print(res)


"""

"""
# 数据统计例子
# li = [11,22,33,44,55,653,3431,312,112]
# # 最小值
# print(min(li))
# # 最大值
# print(max(li))
# # 求和
# print(sum(li))
# # 长度
# print(len(li))

# 高阶内置函数
# eval():去引号
# print(eval("11+22"))
#
# # 获取l列表中的索引和对应的值
# li = ["java", "python"]
# res = enumerate(li)
# print(list(res))
#
# for i in li:
#     print(li.index(i), i)
#
# for i,v in enumerate(li):
#     print(i,v)

# zip数据的聚合打包,聚合后的数据只能使用一次
# content = ["name", "age", "gender"]
# data = ["jack", 18, "man"]
# res = zip(content, data)
# res2 = list(res) # 重复使用
# print(dict(res))

# 拓展(列表聚合成数组)，聚合长度以最短的作为基准
# li = [11,22,33]
# li2 = [1,3]
# li3 = [111,222,333]
# res = zip(li,li2,li3)
# print(list(res))

# 过滤器filter()
"""
作用：
    批量过滤数据
    参数1：过滤规则（函数）
    参数2：需要过滤的数据
"""
# 需求：大于80的提取
great = [55, 67, 86, 98, 76, 60, 87]
# result = []
# for i in great:
#     if i > 80:
#         result.append(i)
# print(result)

# def func(x):
#     return x>80
#
#
# print(func(79))
#
# li = filter(func,great)
# print(list(li))

# 应用场景
# res = filter(lambda x: x > 80, great)
# print(list(res))


# 列表排序拓展
# 此法，仅为元祖中第一个元素的大小进行排序，并非全部
li = [(11, 22, 33), (9, 8, 55), (3, 122, 45)]
li.sort()
print(li)

# 中间位置的元素排序
# def func(x):
#     return x[1]
#
# li.sort(key=lambda x:x[1]) # 简便函数方法
#
# li.sort(key=func)
# print(li)

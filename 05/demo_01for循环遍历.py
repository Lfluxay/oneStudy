"""
    for
        遍历列表
        遍历字典

"""
# 遍历列表
# l = [1,2,3,4,5,5,6,7]
# for i in l:
#     if i > 0:
#         print("t")
#     else:
#         print("f")


# 遍历字典,默认是比键
dic = {"a": "1", "b": "2", "c": "3"}
# 键
# for i in dic.values():
#     print(i)
#
# # 值
# for i in dic.keys():
#     print(i)

# 键值对
# for i in dic.items():
# for k,v in dic.items():
#     print("key:",k,"value:",v)

# 元组拆包
t = ("jack", 12, "man",)
k, v, m = t
print("name:", k, "age:", v, "gender:", m)

# 遍历字符串
# for i in "sasdaewqeq":
#     print(i)

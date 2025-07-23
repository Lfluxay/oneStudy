"""
需求：
操作data.txt文件
    转换数据格式
"""

# def func1():
#     with open(file="data.txt", mode="r", encoding="utf-8")as f:
#         datas = f.readlines()
#     res = {}
#     # 同时获取索引和值
#     for i, v in enumerate(datas):
#         # 传入索引数据
#         key = "data{}".format(i)
#         # 传入值，且全员替换换行符
#         value = v.replace("\n", '')
#         # 键值匹配
#         res[key] = value
#     return res
#
# print(func1())
"""
1.转为字典形式的列表
2.转为带索引的列表
"""


def func():
    with open(file="test_data.txt", mode="r", encoding="utf-8") as f:
        data = f.readlines()
    # 数据转为一个列表，空列表接受数据
    res = []
    # 遍历每行数据
    for i in data:
        # 传入值，且全员替换换行符
        i = i.replace("\n", '')
        # 使用函数切割，分成一个列表
        itme = i.split(",")
        # 创建字典存储数据
        dic = {}
        for j in itme:
            # 分割键
            key = j.split(":")[0]
            # 分割值
            value = j.split(":")[1]
            # 键值配对
            dic[key] = value
            # 添加到列表
        res.append(dic)
    return res


def func1(datas):
    dic = {}
    for i in range(len(datas)):
        dic["data{}".format(i + 1)] = datas[i]
    return dic


if __name__ == "__main__":
    datas = func()
    print(datas)

    res = func1(datas)
    print(res)
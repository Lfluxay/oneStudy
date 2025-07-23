"""
使用场景，for遍历使用

    keys：
        获取所有的键,取出后转换数据类型

    values：
        获取所有的值,取出后转换数据类型

    items：
        同时获取所有的键值对,元组形式返回数据

    copy:
        用的少

"""
dic = {"name": "jack","age": 18,"gender": "男"}
dic2 = dic.copy()
res = list(dic.keys())
vle = list(dic.values())
it = list(dic.items())
print(res)
print(vle)
print(it)

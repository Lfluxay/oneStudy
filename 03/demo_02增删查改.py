"""
字典中的值可是任意类型的数据

增：
    通过键进行赋值
    update:一次性增加多个kv对,更新内容
删：
    pop:指定键进行删除（返回删除的元素对应的值）
    popitem：删除最后一个加入的元素
    clear：清空字典

查：
    通过键进行查找
    get方法，键不存在则不会报错

改：
    对键进行赋值(有则改，无则增)

"""

# 增-----------
# 1.键值增加
# dic = {}
# dic["skill"] = 'python'
# print(dic)
#
# # 2.update添加
# dic.update({"name":"jcak","age":18})
# print(dic)


# 改-----------
# dic = {"name": "jcak","age": 18}
# dic["name"] = "rose"
# print(dic)


# 删------------
# dic = {"name": "jcak","age": 18}
# # pop,指定键删除----
# res = dic.pop("age")
# print(res)
# print(dic)

# popitem删除最后一个加入的元素，元组的形式返回被删除的键值对
# dic = {"name": "jcak","age": 18}
# dic["a"] = 100
# dic["b"] = 99
# res = dic.popitem()
# print(dic)
# print(res)

# clear----
# dic = {"name": "jcak","age": 18}
# dic.clear()
# print(dic)


# 查--------
# dic = {"name": "jcak","age": 18}
# # 键查找值,键不存在则会报错
# print(dic["name"])
# # get方法，键不存在则不会报错
# print(dic.get("name"))

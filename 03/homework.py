"""
1.注册某个网站，需要填写个人信息，编写一段代码要求如下：
    运行时分别提醒输入姓名，性别，年龄，输入之后将数据存储为字典数据
    数据存储之后，然后输出个人介绍，格式如下：我的名字xxx，今年xxx岁，性别xx，喜欢敲代码
    平台需要补充身高和联系方式的信息，添加这些信息
    为了保护隐私，需要删除联系方式
"""
# name = input("请输入姓名:")
# gender = input("请输入性别:")
# age = input("请输入年龄:")
# user_info = {"name":name,"gender":gender,"age":age}
# print(
#     "我的名字{}，今年{}岁，性别{}，喜欢敲代码".format(user_info["name"],user_info["gender"],user_info["age"])
# )

# user_info["height"] = input("请输入身高：")
# user_info["number"] = input("请输入联系方式：")
# print(user_info)
#
# user_info.pop("number")
# print(user_info)


# 取嵌套数据
# data = {
#    "errcode": 0,
#    "errmsg": "ok",
#    "department":
#        {
#            "id": 2,
#            "name": "广州研发中心",
#            "name_en": "RDGZ",
#            "parentid": 1,
#            "order": 10
#        },
#     "name": "邮箱产品部",
# }
#
# name = data["department"]["name"]
# print(name)

"""
有如下几个数据：t1 = ("aa",11) t2 = ("bb",22) t3 = [("cc",11)]
请对上面数据进行相关操作，得到{"aa",11，"bb",22，"cc",11}
"""
# 列表添加数据，转换为字典
# t1 = ("aa",11)
# t2 = ("bb",22)
# t3 = [("cc",11)]
# t3.insert(0,t1)
# t3.insert(1,t2)
# data = dict(t3)
# print(data)


# 现在有列表li1 = [111，22，33，343，121，22，33，111，22，121，99]，去重
# li1 = [111,22,33,343,121,22,33,111,22,121,99]
# li2 = list(set(li1))
# print(li2)
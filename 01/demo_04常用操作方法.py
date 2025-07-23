"""
方法：数据对象.方法名()


常用方法：
    format:格式化方法
    replace:替换
        用法：replace(被替换参数，需替换参数，指定替换次数)
        注意：被替换内容只能传递字符串
    find:查找指定字符的索引位置，重复则返回第一个
    join:字符串拼接
        "".join((x1,x2,x3)),x是参数
    split:分割成为多个字符
        .split("分割处内容")
    strip:去除首位字符内容，可指定前后,+r or + l
    lower:大写转小写
    upper:小写转大写


"""

# # 替换字符串的123为999,默认替换所有
# s = "123456789123"
# print(s.replace("123","999",1))
#
# # find
# s = "pythonA java php"
# print(s.find("j",7,-1))
#
# # join拼接
# s1 = "test"
# s2 = "python"
# s3 = "java"
# print('_'.join((s1, s3, s2)))
#
# # split用法
# s = "python java php c++"
# print(s.split(" "))
#
# # 去除空白或字符（首位去除）
# s = "--------python hello-------"
# print(s.strip("-"))
# s = "--------python hello-------"
# print(s.lstrip("-"))
#
#
# # 转换大小写
# s = "--------pythoAn hello-------"
# print(s.lower())
# print(s.upper())

s = "pythonA java php"
print(s.find("A"))
import re
"""
# 引入
str1 = "asdsaijdos13300998899aodjas iodjsa    da"

# 非正则语法
# res = re.findall("13300998899", str1)

"""
# 正则表达式的语法介绍
"""
# ---—————常见的单字符（元字符）—————————————————————————————————————————
# \d，表示一个数字，后面加{}，括号内的是数字的长度
res = re.findall("\d{11}", str1)
print(res)

# \D，表示一个非数字,后面加{}，括号内的是数字的长度
res1 = re.findall("\D{3}", str1)
print(res1)

# \s，表示一个空白字符
res3 = re.findall("\s", str1)
print(res3)

# \S,表示一个非空白字符
res4 = re.findall("\S", str1)
print(res4)

# \w，匹配一个单词字符（数字，字母，下划线）
res5 = re.findall("\w", str1)
print(res5)

# \W,表示一个非单词字符，除数字，字母，下划线的所有字符
res6 = re.findall("\W", str1)
print(res6)

# (.),表示任意字符的匹配，通配符
res7 = re.findall(".", str1)
print(res7)

# [],举例匹配的单字符,范围用-
res8 = re.findall("[1-9]", str1)
print(res8)


# ---—————表示数量—————————————————————————————————————————
s1 = '123aacma112233.123456'

res = re.findall("\d{5}", s1)
print(res)

{n},匹配长度为n，超出长度不取
{n,},匹配长度为n以上，包含n
{n,m},匹配长度为n和m之间,包含n和m本身,匹配完后有剩余，则按最高指定长度匹配，直到长度不够泽则降位匹配
可以在后面添加？取消贪婪匹配模式，默认是贪婪匹配模式



# -----------------------------贪婪模式的应用-----------------------------
params = '{"id": "#id#", ' \
         '"name": "#name#", ' \
         '"data": "#data#", ' \
         '"title": "#title#", ' \
         '"a": 11, "b": 22}'

res = re.findall("#.{1,}?#", params)
print(res)


# +,表示一次以上  =====   #.{1,}?#
res1 = re.findall("#.+?#", params)
print(res1)


# *，表示0此以上
s = '123abc'
r = re.findall("\d*", s)
print(r)

"""
# ___________________________表示边界_____________________________
"""
字符串边界：
        ^,表示字符串的开头（起始位置）
        $,表示字符串的结尾（终止位置）
        
        
单词边界：
        \b,表示单词的开头（起始位置）
        \B,表示非单词的结尾（终止位置）        
        
"""
# s = "123python456javac++123"

# res = re.findall('^123',s)
# print(res)

# res = re.findall('123$',s)
# print(res)

#s = 'python is good?java'
# res = re.findall(r'\bpython',s)
# print(res)

# s = '123pythonn is good?java'
# res = re.findall(r'python\B', s)
# print(res)

# ___________________________表示边界_____________________________
"""
表示分组
    （）：
"""

# params = '{"id": "#id#", "name": "#name#","data": "#data#","title": "#title#", "a": 11, "b": 22}'
#
# res = re.findall('#.+?#', params)
# print(res)
#
# res = re.findall('#(.+?)#', params)
# print(res)


# s = 'foepwkfwemda1BBBaa123aa-aa678aa-aa789aaBBBdsanod;ashdoa;'

# res = re.findall('BBB.+?BBB', s)
# print(res)
# res = re.findall('BBB(.+?)BBB', s)
# print(res)
# res = re.findall('aa(.+?)aa', s)
# print(res)








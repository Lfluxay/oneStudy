import re
class Test01:
    id = 10
    name = "jack"
    data = "001"
    title = "ok"

params = '{"id": "#id#", ' \
         '"name": "#name#", ' \
         '"data": "#data#", ' \
         '"title": "#title#", ' \
         '"a": 11, "b": 22}'

# 当前存在的问题：每次需要替换的参数都需要调用一次replace方法
# params = params.replace("#id#", str(Test01.id))
# params = params.replace("#name#", str(Test01.name))
# params = params.replace("#data#", str(Test01.data))
# params = params.replace("#title#", str(Test01.title))
# print(params)

res = re.findall("#.+?#", params)

# 正则表达式匹配邮箱

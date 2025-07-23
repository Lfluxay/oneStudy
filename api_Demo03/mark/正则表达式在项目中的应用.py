import re
class TestData:
    id = 123
    name = 'jack'
    data = 'abc'
    title = 'testcase'
params = '{"id": "#id#", "name": "#name#","data": "#data#","title": "#title#", "a": 11, "b": 22}'

# findall,匹配符合规则的数据，列表返回
res = re.findall('#.+?#', params)
print(res)

# search，方法，匹配并返回一个符合规则的匹配对象
res2 = re.search('#(.+?)#', params)
print(res2)
# 提取匹配对象中的内容
# group，提取匹配对象中的内容
item = res2.group()
print("被替换内容：", item)
attr = res2.group(1)
print("被替换属性名：", attr)
value = getattr(TestData, attr)
print('获取出来类属性值：', value)
param = params.replace(item, str(value))
print(param)


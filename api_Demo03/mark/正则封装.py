import re
class TestData:
    id = 123
    name = 'jack'
    data = 'abc'
    title = 'testcase'
params = '{"id": "#id#", "name": "#name#","data": "#data#","title": "#title#", "a": 11, "b": 22}'


while re.search('#(.+?)#', params):
    res2 = re.search('#(.+?)#', params)
    print(res2)
    item = res2.group()
    attr = res2.group(1)
    value = getattr(TestData, attr)
    # 进行替换
    params = params.replace(item, str(value))

print(params)



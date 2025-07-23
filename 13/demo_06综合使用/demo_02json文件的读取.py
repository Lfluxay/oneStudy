import json

with open('data.json', 'r', encoding='utf-8') as f:
    # 读取文件的中的数据，并自动转为py中的相关数据类型
    res = json.load(f)
print(res)

data = res['res']
print(data)


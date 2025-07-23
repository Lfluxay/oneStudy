"""
json模块总结
    load:
        读取json文件转为对应的python数据
    loads:
        json字符串转为python数据
    dumps:
        python数据转为json字符串

"""


import json

# python 转  json-----------
dic = {"aa": None, "bb": "python", "cc": True, "dd": [11, 22, 33]}
# python数据[列表或字典]转为json数据【字符串】
res = json.dumps(dic)
print(res)

# json 转  python-----------
js = '{"aa": null, "bb": "python", "cc": true, "dd": [11, 22, 33]}'
# 将json字符串转为对应的Python数据
res = json.loads(js)
print(res)
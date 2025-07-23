"""
什么是局部变量？
    在函数内部定义的变量，仅在函数内使用
什么是全局变量？
    在模块内定义的变量，任意使用
函数内部如何修改全局变量？
    global

"""

"""
请封装一个函数，按要求实现数据的格式转换
传入参数：data = ["{'a':11,'b':2}","[11,22,33,44]"]
返回结果：res = [{'a':11,'b':2},[11,22,33,44]]
通过代码将传入参数转换为返回结果所需的数据，然后返回
"""

def func(data):
    # result = []
    # for i in data:
    #     res = eval(i)
    #     result.append(res)
    # return result
    return [eval(i) for i in data]
data = ["{'a':11,'b':2}","[11,22,33,44]"]
res = func(data)
print(res)


"""
封装一个函数，实现数据转换
传入参数:
    cases = [
    ['case_id','case_title','url','data','success'],
    [1,'case1','www.baidu.com','001','ok'],
    [2,'case2','www.baidu.com','002','ok'],
    [3,'case3','www.baidu.com','002','ok'],
    [4,'case4','www.baidu.com','002','ok'],
    [5,'case5','www.baidu.com','002','ok']
]

返回结果：
    cases02 = [
    ['case_id':1,case_title':'case1','url':'www.baidu.com','data':'001','success':'ok'],
    ['case_id':2,case_title':'case2','url':'www.baidu.com','data':'002','success':'ok'],
    ['case_id':3,case_title':'case3','url':'www.baidu.com','data':'002','success':'ok'],
    ['case_id':4,case_title':'case4','url':'www.baidu.com','data':'002','success':'ok'],
    ['case_id':5,case_title':'case5','url':'www.baidu.com','data':'002','success':'ok']
    ]
"""
def func(cases):
    result = []

    title = cases[0]
    for i in cases[1:]:
        dic =dict(zip(title,i))
        result.append(dic)
    return result

cases = [
    ['case_id','case_title','url','data','success'],
    [1,'case1','www.baidu.com','001','ok'],
    [2,'case2','www.baidu.com','002','ok'],
    [3,'case3','www.baidu.com','002','ok'],
    [4,'case4','www.baidu.com','002','ok'],
    [5,'case5','www.baidu.com','002','ok']
]
res = func(cases)
print(res)


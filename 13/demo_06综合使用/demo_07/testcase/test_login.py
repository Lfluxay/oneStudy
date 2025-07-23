# import unittest
# from testwork_02.homework import register
# from unittestreport import ddt, list_data
#
#
#
# import openpyxl
#
# workbook = openpyxl.load_workbook(r"/Users/scan/Desktop/柠檬班/13/testwork_02/testdata.xlsx")
# sh = workbook["test"]
# # 获取所有行
# res = list(sh.rows)
# # 获取excel中的第一行数据
# title = [i.value for i in res[0]]
# case = []
# # 遍历除第一行外的所有行的数据
# for item in res[1:]:
#     # 获取其他行的数据
#     data = [i.value for i in item]
#     # 第一行的数据和当前的数据打包为字典
#     dic = dict(zip(title,data))
#     # 把字典添加到列表中
#     case.append(dic)
#
#
#
#
# @ddt
# class Register(unittest.TestCase):
#     # 正常注册
#     @list_data(case)
#     def test_register(self, item):
#         # 准备数据
#         expected = eval(item['expected'])
#         params = eval(item['params'])
#         # 调用功能函数，获取实际结果
#         res = register(**params)
#         self.assertEqual(expected, res)
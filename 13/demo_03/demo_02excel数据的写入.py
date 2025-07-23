"""
封装的需求：
    数据读取：
        封装一个可以读取任意Excel文件的方法，可以指定读取的表单
    数据写入：
        文件名：
        表单名：
        行:
        列：
        写入内容：

"""
import openpyxl

workbook = openpyxl.load_workbook("data.xlsx")
sh = workbook['Sheet1']

# 数据写入
sh.cell(row=1, column=1, value="套你猴子")
# 数据保存
workbook.save("data.xlsx")

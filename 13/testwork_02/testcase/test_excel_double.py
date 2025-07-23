import unittest
from testwork_02.homework import register, login_check
from unittestreport import ddt, list_data
from demo_03.handle_excel import HandleExcel



@ddt
class Register(unittest.TestCase):
    excel = HandleExcel(r'/Users/scan/Desktop/柠檬班/13/testwork_02/testdata.xlsx', 'test')
    case = excel.read_data()

    # 正常注册
    @list_data(case)
    def test_register(self, item):
        # 准备数据
        expected = eval(item['expected'])
        params = eval(item['params'])
        row = item['case_id'] + 1
        print("当前用例的行号{}".format(row))
        res = register(**params)
        print(res)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            # 测试结果回写
            print("fail")
            self.excel.write_data(row=row, column=5, value="fail")
            # 主动抛出异常
            raise e
        else:
            print("pass")
            self.excel.write_data(row=row, column=5, value="pass")

@ddt
class Login(unittest.TestCase):
    excel1 = HandleExcel(r'/Users/scan/Desktop/柠檬班/13/testwork_02/testdata.xlsx', 'test01')
    case1 = excel1.read_data()
    print(case1)

    @list_data(case1)
    def test_login(self, item):
        expected = eval(item['expected'])
        params = eval(item['params'])
        row = item['case_id'] + 1
        print("当前用例的行号：", row)
        res = login_check(*params)
        print(res)
        print(res)
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            # 测试结果回写
            print("fail")
            self.excel1.write_data(row=row, column=5, value="fail")
            # 主动抛出异常
            raise e
        else:
            print("pass")
            self.excel1.write_data(row=row, column=5, value="pass")





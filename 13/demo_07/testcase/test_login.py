import unittest
from testwork_02.homework import login_check
from unittestreport import ddt, list_data
from demo_03.handle_excel import HandleExcel
from demo_04_log.handle_log import my_log



@ddt
class Register(unittest.TestCase):
    excel = HandleExcel(r'/Users/scan/Desktop/柠檬班/13/demo_07/testdata.xlsx', 'test01')
    case = excel.read_data()

    # 正常注册
    @list_data(case)
    def test_register(self, item):
        # 准备数据
        expected = eval(item['expected'])
        params = eval(item['params'])
        row = item['case_id'] + 1
        res = login_check(*params)

        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            # 测试结果回写
            self.excel.write_data(row=row, column=5, value="fail")
            # 日志输出
            my_log.error("用例---【{}】---执行失败".format(item['title']))
            # 非详细异常信息输出
            # my_log.error(e)
            # 详细异常信息输出
            my_log.exception(e)
            # 主动抛出异常
            raise e
        else:
            self.excel.write_data(row=row, column=5, value="pass")
            my_log.info("用例---【{}】---执行成功".format(item['title']))


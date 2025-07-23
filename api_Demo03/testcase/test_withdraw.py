"""

"""
import unittest
import os
import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handle_log import my_log
from common.handle_assert import Assert
from common.hande_sql import DBUtil

@ddt
class TestWithdraw(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "apidata.xlsx"), "withdraw")
    cases = excel.read_data()
    assertD = Assert()
    db = DBUtil()

    @classmethod
    def setUpClass(cls):
        """用例类的前置方法：登录提取token"""
        # 1.请求登录接口,进行登录
        url = conf.get("env", "base_url") + "/member/login"
        # 配置文件读取账号
        params = {
            "mobile_phone": conf.get("test_data", "mobile"),
            "pwd": conf.get("test_data", "pwd")

        }
        headers = eval(conf.get("env", "headers"))
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        # 2.登录成功之后提取token
        # 匹配之后是列表，利用索引取值
        token = jsonpath(res, "$..token")[0]
        # token添加至请求头
        headers["Authorization"] = "Bearer " + token
        # 设置请求头为类属性
        cls.headers = headers
        # setattr(TestRecharge, "headers", headers)
        # 3.提取用户ID
        cls.member_id = jsonpath(res, "$..id")[0]

    @list_data(cases)
    def test_withdraw(self, item):
        # 1.准备数据
        url = conf.get("env", "base_url") + item["url"]

        """动态处理需要进行替换的参数"""
        item["data"] = item["data"].replace("#member_id#", str(self.member_id))
        # print(item["data"])
        """--------------------------------"""
        params = eval(item["data"])
        expected = eval(item["expected"])
        method = item["method"].lower()
        row = item["case_id"] + 1


        # --------------------------取现之前查询用户余额-----------------------------------
        sql = 'SELECT leave_amount FROM futureloan.member WHERE mobile_phone="{}"'.format(conf.get("test_data", "mobile"))
        # 取现前前查询金额
        start_amount = self.db.exe_sql_one(sql)[0]
        print("用例执行之前，用户的余额为{}".format(start_amount))


        # 发送请求，获取返回数据
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        # 断言
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))
        # --------------------------取现之后查询用户余额-----------------------------------
        # 取现后查询金额
        end_amount = self.db.exe_sql_one(sql)[0]
        print("用例执行之后，用户的余额为{}".format(end_amount))


        try:
            self.assertD.assertDictIn(expected, res)
            # --------------------------断言账户金额变化值是否等于取现值（根据条件需求进行断言）-----------------------------------
            if item['check_sql']:
                self.assertEqual(float(start_amount - end_amount), float(params['amount']))


        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="fail")
            my_log.error("用例------【{}】------执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="pass")
            my_log.info("用例------【{}】------执行成功".format(item["title"]))

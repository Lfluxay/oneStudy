"""
充值的前提：
    账号登录
        提取token

unittest：
    前置
        setup，setupClass
    后置
        teardown，teardownClass

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
from common.tools import replace_data
from common.hand_sign import HandleSign


@ddt
class TestRecharge(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "apidata.xlsx"), "recharge")
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
        cls.token = jsonpath(res, "$..token")[0]
        # token添加至请求头
        headers["Authorization"] = "Bearer " + cls.token
        # 设置请求头为类属性
        cls.headers = headers
        # setattr(TestRecharge, "headers", headers)
        # 3.提取用户ID
        cls.member_id = jsonpath(res, "$..id")[0]

    @list_data(cases)
    def test_recharge_sign(self, item):
        # 1.准备数据
        url = conf.get("env", "base_url") + item["url"]

        """动态处理需要进行替换的参数"""
        # 正则匹配写法
        item['data'] = replace_data(item['data'], TestRecharge)
        # 一般写法
        # item["data"] = item["data"].replace("#member_id#", str(self.member_id))
        # print(item["data"])
        """--------------------------------"""
        params = eval(item["data"])

        # -----------RSA加密补充部分----------
        par_sign = HandleSign.generate_sign(self.token)
        print("签名和时间戳：{}".format(par_sign))
        params.update(par_sign)
        # ----------------------------------


        expected = eval(item["expected"])
        method = item["method"].lower()
        # --------------------------请求接口之前查询用户余额-----------------------------------
        sql = 'SELECT leave_amount FROM futureloan.member WHERE mobile_phone="{}"'.format(conf.get("test_data", "mobile"))
        # 充值前查询金额
        start_amount = self.db.exe_sql_one(sql)[0]
        print("用例执行之前，用户的余额为{}".format(start_amount))


        row = item["case_id"] + 1
        # 发送请求，获取返回数据
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()
        # 断言
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))

        # -----------------------请求接口之后查询用户余额-----------------------------------
        # 查询充值后金额
        end_amount = self.db.exe_sql_one(sql)[0]
        print("用例执行之后，用户的余额为{}".format(end_amount))

        try:
            # 断言预期结果和实际结果
            self.assertD.assertDictIn(expected, res)
            # -------------------校验数据库中用户余额的变化是否等于充值的金额(每条用例都执行此断言)-----------------------------------
            if res['msg'] == "OK":
                # 数据库断言：如果充值成功，对充值金额进行断言
                self.assertEqual(float(end_amount - start_amount), float(params['amount']))
                print("本次充值成功，充值{}元".format(params['amount']))
            else:
                # 失败则充值金额为0
                self.assertEqual(float(end_amount - start_amount), 0)
                print("本次充值失败，充值{}元".format(0))



        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value="fail")
            my_log.error("用例------【{}】------执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="pass")
            my_log.info("用例------【{}】------执行成功".format(item["title"]))

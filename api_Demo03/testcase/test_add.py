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
class TestAdd(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "apidata.xlsx"), "add")
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
        print(res)
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
    def test_add(self, item):
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

        """调用接口之前，查询数据库，看项目数量"""
        sql = "SELECT * FROM futureloan.loan where member_id={}".format(self.member_id)
        start_count = self.db.exe_sql_count(sql)
        print("调用接口之前的项目数量：{}".format(start_count))

        # 发送请求，获取返回数据
        response = requests.request(method=method, url=url, json=params, headers=self.headers)
        res = response.json()

        """调用接口之后，查询数据库，查看项目数量"""
        end_count = self.db.exe_sql_count(sql)
        print("调用接口之后的项目数量：{}".format(end_count))



        # 断言
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))


        try:
            # 断言预期结果和实际结果
            self.assertD.assertDictIn(expected, res)

            """根据数据库查询结果，进行断言"""
            if res['msg'] == 'OK':
                self.assertEqual(end_count - start_count, 1)
            # 校验失败
            # else:
            #     self.assertEqual(end_count - start_count, 0)
        except AssertionError as e:
            # 测试结果回写
            self.excel.write_data(row=row, column=8, value="fail")
            # 打印日志信息
            my_log.error("用例------【{}】------执行失败".format(item["title"]))
            # 打印日志详细异常
            my_log.exception(e)
            # 抛出异常
            raise e
        else:
            self.excel.write_data(row=row, column=8, value="pass")
            my_log.info("用例------【{}】------执行成功".format(item["title"]))

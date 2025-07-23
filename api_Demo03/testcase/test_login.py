import unittest
import os
import requests
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handle_log import my_log
from common.handle_assert import Assert
from common.tools import replace_data

@ddt
class TestLogin(unittest.TestCase):
    # 读取用例数据
    excel = HandleExcel(os.path.join(DATA_DIR, "apidata.xlsx"), "login")
    cases = excel.read_data()
    assertD = Assert()

    # 读取url
    base_url = conf.get("env", "base_url")
    # 读取请求头
    headers = eval(conf.get("env", "headers"))

    @list_data(cases)
    def test_login(self, item):
        # 一、准备用例数据
        # 1.接口地址
        url = self.base_url + item["url"]
        # 2.请求参数
        # 参数替换
        # ------------升级前的代码-----------
        # item["data"] = item["data"].replace("#mobile#", conf.get('test_data', 'mobile'))

        # ------------升级后的代码-----------
        item['data'] = replace_data(item['data'], TestLogin)
        params = eval(item["data"])


        # 3.请求方法
        method = item["method"].lower()
        # 4.请求头（类属性中配置好了,调用即可）
        head = self.headers
        # 5.用例预期结果
        expected = eval(item["expected"])
        row = item["case_id"] + 1

        # 二、请求结果，获取返回结果
        response = requests.request(method, url, json=params, headers = head)
        res = response.json()
        # 断言
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))
        try:
            # 断言code和msg
            # self.assertEqual(expected["code"], res["code"])
            # self.assertEqual(expected["msg"], res["msg"])
            self.assertD.assertDictIn(expected, res)
        except AssertionError as e:
            # 回写结果
            self.excel.write_data(row=row, column=8, value="fail")
            # 失败抛出异常，打印日志
            my_log.error("用例----[{}]----执行失败".format(item['title']))
            my_log.exception(e)
            raise e

        else:
            # 成功回写结果
            self.excel.write_data(row=row, column=8, value="pass")
            # 输出日志
            my_log.error("用例----[{}]----执行成功".format(item['title']))
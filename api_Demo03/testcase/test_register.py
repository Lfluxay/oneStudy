import unittest
import os
import requests
import random
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.handle_log import my_log
from common.handle_assert import Assert
from common.hande_sql import DBUtil
from common.tools import replace_data



@ddt
class TestRegister(unittest.TestCase):
    # 读取用例数据
    excel = HandleExcel(os.path.join(DATA_DIR, "apidata.xlsx"), "register")
    cases = excel.read_data()
    assertD = Assert()
    # 读取url
    base_url = conf.get("env", "base_url")
    # 读取请求头
    headers = eval(conf.get("env", "headers"))
    # 实例化操作数据库对象
    db = DBUtil()


    @list_data(cases)
    def test_register(self, item):
        pass
        # 一、准备用例数据
        # 1.接口地址
        url = self.base_url + item["url"]
        """动态生成手机号码"""
        # 判断手机号码是否存在数据中
        # 方法1
        if "#mobile#" in item["data"]:
            phone = self.mobile()
            item["data"] = item["data"].replace("#mobile#", phone)
        # 方法2
        # if "#mobile#" in item["data"]:
        #     setattr(TestRegister, 'mobile', self.mobile())
        #     item["data"] = replace_data(item['data'], TestRegister)
        # print(item['data'])
        """--------------------------"""
        # 2.请求参数
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
        # 查询数据库中的账号数量,方法1
        # sql = 'SELECT * FROM futureloan.member WHERE mobile_phone="{}"'.format(params.get("mobile_phone", ""))
        # count = self.db.exe_sql_count(sql)
        # 方法2
        if item['check_sql']:
            s = item['check_sql'].format(params.get('mobile_phone', ""))
            sql = s.replace("\'", '')
            count = self.db.exe_sql_count(sql)


        # 断言
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))
        try:
            # 断言code和msg
            # self.assertEqual(expected["code"], res["code"])
            # self.assertEqual(expected["msg"], res["msg"])
            # 使用成员断言
            self.assertD.assertDictIn(expected, res)
            # 判断数据是否需要校验
            if item["check_sql"]:
                print("数据库中查询的数量为：", count)
                self.assertEqual(1, count)

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


    def mobile(self):
        """随机生成手机号码"""
        phone = str(random.randint(13800000000, 13899999999))
        return phone

        # mobile = "133"
        # for i in range(8):
        #     n = str(random.randint(0, 9))
        #     mobile += n


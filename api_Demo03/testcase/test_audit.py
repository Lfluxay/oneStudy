
"""
审核接口:   管理员去审核

添加项目：
    1.前置：
        用户登录（类级别前置）
    2.测试用例方法的编写

审核的前置条件：
    两个不同的角色用户（类级别前置）
        分别进行登录，提取token和用户的ID

    1.管理员登录(类级别的前置)
            审核需要管理员权限
                admin_token
                admin_member_id
                admin_headers

    2.普通用户的角色去添加项目
            普通用户添加项目
        1)普通用户的登录
        2)创建一个项目

        添加项目：（用例级别的前置）
            每次添加一个项目，提取loan_id保存为类属性

        用例方法：
            用例之前做了数据依赖的处理，审核不是审核状态的项目
                判断是否是审核通过的项目，并且结果是审核通过，如果是则保存项目ID为审核通过项目ID

"""
import random
import unittest
import os
import requests
from jsonpath import jsonpath
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from common.tools import replace_data
from common.handle_assert import Assert
from common.handle_log import my_log
from common.hande_sql import DBUtil


@ddt
class TestAudit(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATA_DIR, "apidata.xlsx"), 'audit')
    cases = excel.read_data()
    assertD = Assert()
    db = DBUtil()

    # 类级别前置
    @classmethod
    def setUpClass(cls) -> None:
        """登录前置"""
        # ------------------管理员登录------------------
        # 1.准备登录的数据
        url = conf.get("env", 'base_url') + '/member/login'
        params = {
            "mobile_phone": conf.get('test_data', 'admin_mobile'),
            "pwd": conf.get('test_data', 'admin_pwd')
        }
        headers = eval(conf.get('env', 'headers'))
        # 2.请求登录接口
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()

        # 3.提取token，放到请求头中，后续调用
        admin_token = jsonpath(res, "$..token")[0]
        headers['Authorization'] = 'Bearer ' + admin_token
        cls.admin_headers =headers
        # 4.提取用户ID
        cls.admin_member_id = jsonpath(res, '$..id')[0]


        # ------------------普通用户登录------------------
        # 1.准备登录的数据
        url = conf.get("env", 'base_url') + '/member/login'
        params = {
            "mobile_phone": conf.get('test_data', 'mobile'),
            "pwd": conf.get('test_data', 'pwd')
        }
        headers = eval(conf.get('env', 'headers'))
        # 2.请求登录接口
        response = requests.post(url=url, json=params, headers=headers)
        res = response.json()
        # 3.提取token，放到请求头中，后续调用
        token = jsonpath(res, "$..token")[0]
        print(token)
        headers['Authorization'] = 'Bearer ' + token
        cls.headers=headers
        # 4.提取用户ID
        cls.member_id = jsonpath(res, '$..id')[0]

    #用例级别前置
    def setUp(self) -> None:
        """添加项目"""
        # 1、准备数据
        url = conf.get("env", "base_url") + '/loan/add'
        params = {
                "member_id": self.member_id,
                "title": "投资实现财富自由" + str(random.randint(1, 3)),
                "amount": 5000,
                "loan_rate": 18,
                "loan_term": 12,
                "loan_date_type": 1,
                "bidding_days": 10}

        # 2、请求添加项目的接口
        response = requests.post(url=url, json=params, headers=self.headers)
        res = response.json()

        # 3、提取项目的id,保存为类属性
        TestAudit.loan_id = jsonpath(res, '$..id')[0]
        # 动态设置属性
        # setattr(TestAudit, 'loan_id')


    @list_data(cases)
    def test_audit(self, item):
        # print("执行当前用例，累属性中的loan_id{}".format(self.loan_id))
        # 1.准备数据
        url = conf.get("env", 'base_url') + item["url"]
        item['data'] = replace_data(item['data'], TestAudit)
        params = eval(item["data"])
        method = item['method']
        expected = eval(item['expected'])
        row = item['case_id'] + 1
        # 2、请求接口
        response = requests.request(method=method, url=url, json=params, headers=self.admin_headers)
        res = response.json()
        # print(res)

        # 判断用例是否是通过的用例,如果是则保存通过的项目ID
        # if item['app'] == 'true' and res['msg'] == 'OK':
        # 也可以判断审核状态是否是tue
        if item['title'] == '审核成功' and res['msg'] == 'OK':
            TestAudit.pass_loan_id = self.loan_id
            # 方法2，从参数中提取出来
            # TestAudit.loan_id = params['loan_id']

        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))

        # 3.断言
        try:
            self.assertEqual(expected["code"], res["code"])
            self.assertEqual(expected["msg"], res["msg"])
            # 成员断言不适用，会调用封装模块的断言
            # self.assertD.assertDictIn(expected, res)
            if item['check_sql']:
                sql = item['check_sql'].format(self.loan_id)
                status = self.db.exe_sql_one(sql)[0]
                print("数据库中的状态:{}".format(status))
                self.assertEqual(expected['status'], status)

        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value='fail')
            my_log.error("用例------【{}】------执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value='pass')
            my_log.info("用例------【{}】------执行成功".format(item["title"]))





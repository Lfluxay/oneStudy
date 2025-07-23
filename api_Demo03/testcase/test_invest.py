"""
前置操作：
    1.普通用户登录----类级别
    2.管理员登录----类级别
    3.添加项目---类级别
    4.审核项目----类级别

用例前置操作的封装优化：
    1.把多个用例需要使用的一些前置操作封装到一个类中
    2.需要使用这个前置步骤的测试类，直接去继承(多继承)封装好的前置步骤方法
    3.在类级别前置和用例级别的前置，调用对应的方法即可


用例方法：
    1.准备数据
    2.发送请求
    3.断言

# 数据校验
    用户表：
        用户的余额投资前后会发生变化
            投资前 - 投资后 == 投资的金额

    流水记录表：
        投资成功会新增一条流水记录
            投资后的流水记录数量 - 投资前的流水记录数量 == 1

    投资表：
        投资成功会新增一条投资记录
            投资后用户记录数量 - 投资前用户记录记录数量 == 1


    ----拓展-----:
        投资后（可投金额为0）满标的情况下，会生成回款计划
        1.先把项目的投资记录ID都查询出来
        2.遍历投资记录ID
        3.根据每个投资记录的id去查询是否生成回款计划表



"""
import os
import unittest
import requests
from unittestreport import ddt, list_data
from common.handle_excel import HandleExcel
from common.handle_path import DATA_DIR
from common.handle_conf import conf
from testcase.fixture import BaseTest
from common.tools import replace_data
from common.handle_log import my_log
from common.hande_sql import DBUtil

@ddt
class TestInvest(unittest.TestCase, BaseTest):
    excel = HandleExcel(os.path.join(DATA_DIR, 'apidata.xlsx'), 'invest')
    cases = excel.read_data()
    db = DBUtil()

    # 前置登录
    @classmethod
    def setUpClass(cls) -> None:
        # 管理员登录
        cls.admin_login()
        # 普通用户登录
        cls.user_login()
        # 添加项目
        cls.add_project()
        # 审核项目
        cls.audit()

    @list_data(cases)
    def test_invest(self, item):
        # 1、准备用例数据
        url = conf.get('env', 'base_url') + item['url']
        item['data'] = replace_data(item['data'], TestInvest)
        params = eval(item['data'])
        expected = eval(item['expected'])
        method = item['method']
        row = item['case_id'] + 1
        # --------------投资前查询数据库------------------
        # 查询用户表的sql
        sql1 = 'SELECT leave_amount FROM futureloan.member WHERE id="{}"'.format(self.member_id)
        # 查投资记录的sql
        sql2 = 'SELECT id FROM futureloan.invest WHERE member_id="{}"'.format(self.member_id)
        # 查流水记录的sql
        sql3 = 'SELECT id FROM futureloan.financelog WHERE pay_member_id="{}"'.format(self.member_id)
        if item["check_sql"]:
            start_amount = self.db.exe_sql_one(sql1)[0]
            print("投资前的用户余额：{}".format(start_amount))
            start_invest = self.db.exe_sql_count(sql2)
            print("投资前的流水记录数量：{}".format(start_invest))
            start_financelog = self.db.exe_sql_count(sql3)
            print("投资前用户记录数量：{}".format(start_financelog))

        # 2、发送请求
        response = requests.request(url=url, method=method, json=params, headers=self.headers)
        res = response.json()
        print("预期结果：{}".format(expected))
        print("实际结果：{}".format(res))

        # 投资后查询数据库
        if item["check_sql"]:
            end_amount = self.db.exe_sql_one(sql1)[0]
            print("投资后的用户余额：{}".format(end_amount))
            end_invest = self.db.exe_sql_count(sql2)
            print("投资后的流水记录数量：{}".format(end_invest))
            end_financelog = self.db.exe_sql_count(sql3)
            print("投资后用户记录数量：{}".format(end_financelog))


        # 3、断言
        try:
            self.assertEqual(expected['code'], res['code'])
            # 断言实际结果中的是否包含预期中的
            self.assertIn(expected['msg'], res['msg'])
            # 断言查询的数据结果
            if item["check_sql"]:
                # 断言用户余额
                self.assertEqual(params['amount'], float(start_amount - end_amount))
                # 断言投资记录
                self.assertEqual(1, end_invest - start_invest)
                # 断言流水记录
                self.assertEqual(1, end_financelog - start_financelog)
        except AssertionError as e:
            self.excel.write_data(row=row, column=8, value='fail')
            my_log.error("用例------【{}】------执行失败".format(item["title"]))
            my_log.exception(e)
            raise e
        else:
            self.excel.write_data(row=row, column=8, value='pass')
            my_log.info("用例------【{}】------执行成功".format(item["title"]))



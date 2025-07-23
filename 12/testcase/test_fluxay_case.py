"""
测试套件

"""
import unittest
from demo_01 import login_check

class TestLoginFluxay(unittest.TestCase):

    def test_login(self):
        # 1.准备用例数据
        params = {'username':'admin','password':'123456'}
        expected = {'code': 0, 'msg': '登录成功!'}

        # 2.调用被测的功能函数，获取实际结果(发送请求调用接口)
        result = login_check(**params)
        # 非拆包方法
        # login_check(username=params['username'],password=params['password'])

        # 3.断言
        assert expected == result


    def test_usr_error(self):
        # 1.准备用例数据
        params = {'username':'admin01','password':'123456'}
        expected = {'code': 1, 'msg': '账号或密码不正确!'}
        # 2.调用被测的功能函数，获取实际结果(发送请求调用接口)
        result = login_check(**params)
        # 3.断言
        assert expected == result

    def test_pwd_error(self):
        # 1.准备用例数据
        params = {'username':'admin','password':'123123'}
        expected = {'code': 1, 'msg': '账号或密码不正确!'}
        # 2.调用被测的功能函数，获取实际结果(发送请求调用接口)
        result = login_check(**params)
        # 3.断言
        assert expected == result

class TestRegisterFluxay(unittest.TestCase):
    def test_register(self):
        assert 'yes' == 'yes'

    def test_register_02(self):
        assert '200' == '201'
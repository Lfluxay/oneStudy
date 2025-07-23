import unittest
from login_func import login_check
from unittestreport import ddt, list_data

"""
ddt的使用步骤：
    测试类前面使用：@ddt
    测试方法前使用：@list_data（测试数据）
    在测试方法中定义一个参数，用例接收用例数据

如果要给测试用例添加用例描述，需要在测试数据中添加一个title字段或desc字段
    测试数据需要是字典类型的
"""

cases = [
    {"title": "登录成功", 'expected': {'code': 0, 'msg': '登录成功!'}, 'params': {'username': 'admin', 'password': '123456'}},
    {"title": "登录失败", 'expected': {'code': 1, 'msg': '账号或密码不正确!'}, 'params': {'username': 'admin01', 'password': '123456'}}
]


@ddt
class TestLogin(unittest.TestCase):

    @list_data(cases)
    def test_login(self, item):
        data = item['params']
        expected = item['expected']
        res = login_check(**data)
        self.assertEqual(expected, res)



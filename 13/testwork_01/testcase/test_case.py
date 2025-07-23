import unittest
from testwork_01.homework import register
from unittestreport import ddt, list_data

cases = [
    {"title": "注册成功", 'expected': {'code': 1, 'msg': '注册成功'},
     'params': {'username': 'test001', 'password1': '123456', 'password2': '123456'}},
    {"title": "参数为空", 'expected': {'code': 0, 'msg': '所有参数不能为空'},
     'params': {'username': '', 'password1': '123456', 'password2': '123456'}},
    {"title": "账号已存在", 'expected': {'code': 0, 'msg': '该账号已存在'},
     'params': {'username': 'fluxay', 'password1': '123456', 'password2': '123456'}},
    {"title": "账号长度错误", 'expected': {'code': 0, 'msg': '账号密码长度应在6-18位之间'},
     'params': {'username': 'test', 'password1': '123456', 'password2': '123456'}},
    {"title": "密码长度错误", 'expected': {'code': 0, 'msg': '账号密码长度应在6-18位之间'},
     'params': {'username': 'test002', 'password1': '12345', 'password2': '12345'}},
    {"title": "密码输入不一致", 'expected': {'code': 0, 'msg': '输入两次密码不一致'},
     'params': {'username': 'test003', 'password1': '123456', 'password2': '123455'}},
]

@ddt
class Register(unittest.TestCase):
    # 正常注册
    @list_data(cases)
    def test_register(self, item):
        expected = item['expected']
        data = item['params']
        res = register(**data)
        self.assertEqual(expected, res)



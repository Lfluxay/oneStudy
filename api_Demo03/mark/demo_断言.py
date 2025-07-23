# 同接口,不同用例返回的字段不一样怎么处理？
import unittest


class Demo(unittest.TestCase):
    def test_demo(self):
        # 实际结果
        res = {"code": 0, "msg": "ok", "time": "20211014"}
        # 预期结果
        expected = {"code": 0, "msg": "ok"}
        # 断言
        # self.assertEqual(res["code"], expected["code"])
        # self.assertEqual(res["msg"], expected["msg"])

        # self.assertIn(res, expected)
        self.assertDictIn(expected, res)

    def assertDictIn(self, expected, res):
        for k, v in expected.item():
            if res.get(k) == v:
                pass
            else:
                raise AssertionError("{} not in {}".format(expected, res))


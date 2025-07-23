"""
fixture：
    测试夹具

    用例级别：
        setUp:
        用例级别的前置处理，每条测试用例执行之前都会执行

        tearDown:
        用例级别的后置处理，每条测试用例执行之后都会执行

    测试类级别：
        setUpClass:类级别前置
        tearDownClass:类级别后置



"""
# 用例级别
# import unittest
# class TestFluxay(unittest.TestCase):
#
#     def setUp(self):
#         print("------setup------")
#
#     def tearDown(self) -> None:
#         print("=======teardown======")
#
#
#     def test_01(self):
#         print("------01-------")
#
#     def test_02(self):
#         print("------02-------")
#
#     def test_03(self):
#         print("------03-------")
#
#     def test_04(self):
#         print("------04-------")
#
# if __name__=='__main__':
#     unittest.main()


# 类级别
import unittest
class TestFluxay(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("------setup------")
    @classmethod
    def tearDownClass(cls) -> None:
        print("=======teardown======")

    def setUp(self):
        print("------set------")

    def tearDown(self) -> None:
        print("=======tear======")


    def test_01(self):
        print("------01-------")

    def test_02(self):
        print("------02-------")

    def test_03(self):
        print("------03-------")

    def test_04(self):
        print("------04-------")

if __name__=='__main__':
    unittest.main()
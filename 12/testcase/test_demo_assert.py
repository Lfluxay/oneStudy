import unittest
class TestFluxay(unittest.TestCase):

    def test_01(self):
        print("------01-------")
        # assert 200 == 201
        # 断言两个数据是否相等
        # self.assertEqual(200, 201)

        # 成员断言
        data = ['11', '22']
        n = '111'
        self.assertIn(n,data)


    def test_02(self):
        print("------02-------")


if __name__=='__main__':
    unittest.main()
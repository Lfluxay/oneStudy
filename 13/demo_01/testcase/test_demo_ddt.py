"""
DDT:
    data driver test：数据驱动测试

思想：测试数据和用例代码进行分离，方便后期维护和管理


ddt的使用步骤：
    测试类前面使用：@ddt
    测试方法前使用：@list_data（测试数据）
    在测试方法中定义一个参数，用例接收用例数据


ddt的底层原理:
    保存测试数据
    遍历测试数据，创建用例方法，设置为测试类的实例方法

"""

import unittest
from unittestreport import ddt, list_data

# ---------------示例1---------------------
@ddt
class TestFluxay(unittest.TestCase):

    # @list_data([1, 2, 3])
    # def test_01(self):
    #     pass

    # item接收用例数据
    @list_data(list(range(100)))
    def test_01(self, item):
        print("item:", item)
        pass



case = [
    {"expected": "OK", "data": "11"},
    {"expected": "OK", "data": "22"},
    {"expected": "OK", "data": "33"},
    {"expected": "OK", "data": "44"}
]


@ddt
class TestFluxay(unittest.TestCase):
    # item接收用例数据
    @list_data(case)
    def test_01(self, item):
        # for item in case: 错误示范
        print("item:", item)
        pass


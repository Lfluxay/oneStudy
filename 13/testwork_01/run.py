import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover("testcase")

runner = TestRunner(suite, tester="野狐禅", desc="单元测试", )

runner.run()
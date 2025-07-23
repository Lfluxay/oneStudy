import unittest

from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r"/Users/scan/Desktop/柠檬班/13/project/testcase")

runner = TestRunner(suite,
                    filename = "report.html",
                    report_dir = "/Users/scan/Desktop/柠檬班/13/project/reports",
                    title = '测试报告',
                    tester = '野狐禅',
                    desc = "套你猴子项目测试生成的报告"
)
runner.run()

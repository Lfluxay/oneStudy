import unittest
# 方法1
from unittestreport import TestRunner

suite = unittest.TestSuite()
load = unittest.TestLoader()
suite.addTest(load.discover('testcase'))

runner = TestRunner(suite, tester='野狐禅', desc='套你猴子',title="套你猴子")
runner.run()

# 方法2
# suite = unittest.TestSuite()
# load = unittest.TestLoader()
# suite.addTest(load.discover('testcase'))
#
# from BeautifulReport import BeautifulReport
#
# runner = BeautifulReport(suite)
# runner.report('fluxay')
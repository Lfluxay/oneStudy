from unittestreport import TestRunner
import unittest

suite = unittest.defaultTestLoader.discover(r"demo_01/testcase")
runner = TestRunner(suite)
runner.run()
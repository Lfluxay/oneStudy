import unittest

from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r"/Users/scan/Desktop/柠檬班/13/demo_07/testcase")

runner = TestRunner(suite)

runner.run()
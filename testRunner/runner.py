__author__ = 'shikun'
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
import os
from testRunner.runnerBase import TestInterfaceCase
from testcase.login import testLogin
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_common_web_report(start_test_time, endtime, starttime):
    pass

def runnerCaseWeb():
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(testLogin))
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    runnerCaseWeb()

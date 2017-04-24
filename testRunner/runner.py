__author__ = 'shikun'
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append("..")
import time, datetime
import os
from testRunner.runnerBase import TestInterfaceCase
from testcase.login import testLogin
from testcase.setting import testSetting
from common import report
from common import util
import xlsxwriter
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def _report():
    workbook = xlsxwriter.Workbook('report.xlsx')
    worksheet = workbook.add_worksheet("测试总况")
    worksheet2 = workbook.add_worksheet("测试详情")
    re = report.OperateReport(wd=workbook)
    re.init(worksheet, data=util.DATA)
    re.test_detail(worksheet2, data=util.INFO)
    re.close()
def runnerCaseWeb():
    # init_database()
    starttime = datetime.datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(TestInterfaceCase.parametrize(testLogin))
    suite.addTest(TestInterfaceCase.parametrize(testSetting))
    unittest.TextTestRunner(verbosity=2).run(suite)
    endtime = datetime.datetime.now()
    util.DATA["sum_time"] = str((endtime - starttime).seconds) + "秒"
    util.DATA["test_date"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # destory_database()

if __name__ == '__main__':
    runnerCaseWeb()
    print(util.INFO)
    print(util.DATA)
    _report()
    pass

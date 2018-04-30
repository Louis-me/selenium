# -*- coding: utf-8 -*-

__author__ = 'shikun'
import sys
sys.path.append("..")
from Base.BaseRunner import ParametrizedTestCase
from TestCase.HomeTest import HomeTest
import unittest
from Base.BaseInit import mk_file
from Base.BaseStatistics import countDate, writeExcel
from datetime import datetime
from TestCase.MyTest import MyTest
from TestCase.CnblogsTest import CnblogsTest

def runnerCaseApp():
    start_time = datetime.now()
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(HomeTest))
    suite.addTest(ParametrizedTestCase.parametrize(MyTest))
    # suite.addTest(ParametrizedTestCase.parametrize(CnblogsTest))
    unittest.TextTestRunner(verbosity=2).run(suite)
    end_time = datetime.now()
    countDate(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), str((end_time - start_time).seconds) + "秒")


if __name__ == '__main__':
    mk_file()
    runnerCaseApp()
    writeExcel()

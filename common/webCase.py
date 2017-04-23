__author__ = 'shikun'
# -*- coding: utf-8 -*-
from common import operateYaml as ap, operateElement as bo
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class WebCaseBase():
    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
    def execCase(self, f):
        # logTest = testLog.myLog().getLog()
        getCase = ap.getYam(f)
        go = bo.OperateElement(driver=self.driver)
        _d_report_common = {"test_success": 0, "test_failed": 0, "test_sum": 0} #case的运行次数和性能
        for case in getCase["testcase"]:
            go.operate_element(case) # 操作用例
        if go.findElement(getCase["check"]):
            print("通过")
        else:
            print("失败")
        _d_report_common["test_sum"] += 1
__author__ = 'shikun'
# -*- coding: utf-8 -*-
from common import operateYaml as ap, operateElement as bo
from common import testLog
from common import util
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class WebCaseBase():
    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        self.logTest = testLog.myLog().getLog()
        self.casename = kwargs["casename"]
        self.info = {}
    def execCase(self, f):
        # logger = logTest.getMyLogger()
        getCase = ap.getYam(f)
        go = bo.OperateElement(driver=self.driver)
        for case in getCase["testcase"]:
            go.operate_element(case) # 操作用例
            self.logTest.buildStartLine(case["element_info"]+" "+ case["operate_type"])
        if go.findElement(getCase["check"]):
            self.writeLog(getCase["check"], flag=True)
            util.DATA["pass"] = util.DATA["pass"] + 1
            self.info["result"] = "通过"
        else:
            self.writeLog(getCase["check"], flag=False,testinfo=getCase["testinfo"])
            util.DATA["fail"] = util.DATA["fail"] + 1
            self.info["result"] = "失败"
            self.info["reason"] = "无法找到检查点"
        self.info["id"] = getCase["testinfo"][0]["id"]
        self.info["moudle"] = getCase["testinfo"][0]["moudle"]
        self.info["casename"] = self.casename
        self.info["intr"] = getCase["testinfo"][0]["intr"]

        util.DATA["sum"] = util.DATA["sum"] + 1
        util.INFO.append(self.info)

    def writeLog(self, checks, flag, testinfo=None):
        if type(checks) == list:  # 多检查点
            for item in checks:
                if flag == True:
                    self.logTest.buildStartLine(item["element_info"] + " 成功")
                else:
                    self.logTest.buildStartLine(item["element_info"] + " 失败")
                    _testimg = self.logTest.checkPointNG(driver=self.driver, caseName=testinfo[0]["intr"],
                                              checkPoint=item["element_info"])
                    self.info["img"] = _testimg
        else:  # type(getCase["check"]) == dict: # 单检查点
            if flag == True:
                self.logTest.buildStartLine(checks["element_info"] + " 成功")
            else:
                self.logTest.buildStartLine(checks["element_info"] + " 失败")
                _testimg = self.logTest.checkPointNG(driver=self.driver, caseName=testinfo[0]["intr"],
                                          checkPoint=checks["element_info"])
                self.info["img"] = _testimg
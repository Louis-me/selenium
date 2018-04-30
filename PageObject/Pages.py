from Base.BaseYaml import getYam
from Base.BaseOperate import OperateElement
import time
from Base.BaseElementEnmu import Element as be
import os
from PageObject.SumResult import statistics_result
from Base.BaseError import get_error

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class PagesObjects:
    '''
    page层
    kwargs: WebDriver driver, String path(yaml配置参数)
    isOperate: 操作失败，检查点就失败
    testInfo：
    testCase：
    '''

    def __init__(self, kwargs):
        self.driver = kwargs["driver"]

        if kwargs.get("launch", "0") == "0":  # 若为空， 刷新页面
            self.driver.get(self.driver.current_url)
        self.operateElement = ""
        self.isOperate = True
        self.test_msg = kwargs["test_msg"]
        self.testInfo = self.test_msg[1]["testinfo"]
        self.testCase = self.test_msg[1]["testcase"]
        self.test_check = self.test_msg[1]["check"]
        self.logTest = kwargs["logTest"]
        self.caseName = kwargs["caseName"]
        self.get_value = []
        self.is_get = False  # 检查点特殊标志，结合get_value使用。若为真，说明检查点要对比历史数据和实际数据
        self.msg = ""

    '''
     操作步骤
    '''

    def operate(self):

        if self.test_msg[0] is False:
            self.isOperate = False
            return False
        self.operateElement = OperateElement(self.driver)
        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, self.logTest)
            if not result["result"]:
                msg = get_error({"type": be.DEFAULT_ERROR, "element_info": item["element_info"]})
                print(msg)
                self.testInfo[0]["msg"] = msg
                self.isOperate = False
                return False
            if item.get("is_time", "0") != "0":
                time.sleep(item["is_time"])  # 等待时间
                print("==等待%s秒==" % item["is_time"])
            if item.get("operate_type", "0") == be.GET_VALUE or item.get("operate_type", "0") == be.GET_TEXT:
                self.get_value.append(result["text"])
                self.is_get = True  # 对比数据

        return True

    def checkPoint(self, kwargs={}):
        result = self.check(kwargs)
        statistics_result(result=result, testInfo=self.testInfo, caseName=self.caseName,
                          driver=self.driver, logTest=self.logTest,
                          testCase=self.testCase,
                          testCheck=self.test_check)

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    '''

    def check(self, kwargs):
        result = True
        # if kwargs.get("check_point", "0") != "0":
        #     return kwargs["check_point"]

        if self.isOperate:
            for item in self.test_check:

                resp = self.operateElement.operate(item, self.testInfo, self.logTest)
                # 默认检查点，就是查找页面元素
                if kwargs.get("check", be.DEFAULT_CHECK) == be.DEFAULT_CHECK and not resp["result"]:
                    m = get_error({"type": be.DEFAULT_CHECK, "element_info": item["element_info"], "info": item["info"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break
                # 历史数据和实际数据对比
                if kwargs.get("check", be.DEFAULT_CHECK) == be.COMPARE and self.is_get and resp["text"]\
                        not in self.get_value:  # 历史数据和实际数据对比
                    result = False
                    m = get_error({"type": be.COMPARE, "current": item["element_info"], "history": resp["text"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    break
                #  相反检查点，表示如果检查元素存在就说明失败，如删除后，此元素依然存在
                if kwargs.get("check", be.DEFAULT_CHECK) == be.CONTRARY and resp["result"]:
                    m = get_error({"type": be.CONTRARY, "element_info": item["element_info"], "info": item["info"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break
                # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
                if kwargs.get("check", be.DEFAULT_CHECK) == be.CONTRARY_GETVAL and self.is_get and resp["result"] \
                        in self.get_value:
                    m = get_error(
                        {"type": be.CONTRARY_GETVAL, "current": item["element_info"], "history": resp["text"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break

        else:
            result = False
        return result

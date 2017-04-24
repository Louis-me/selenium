__author__ = 'shikun'
# -*- coding: utf-8 -*-
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait
from common import util as common
# 此脚本主要用于查找元素是否存在，操作页面元素
class OperateElement():
    def __init__(self, driver=""):
        self.driver = driver
    def findElement(self, mOperate):
        '''
        查找元素.mOperate,dict|list
        operate_type：对应的操作
        element_info：元素详情
        find_type: find类型
        '''
        try:
            if type(mOperate) == list:# 多检查点
                for item in mOperate:
                    WebDriverWait(self.driver, common.WAIT_TIME).until(lambda x: elements_by(item, self.driver))
                return True
            if type(mOperate) == dict: # 单检查点
                WebDriverWait(self.driver, common.WAIT_TIME).until(lambda x: elements_by(mOperate, self.driver))
                return True
        except selenium.common.exceptions.TimeoutException:
            return False
        except selenium.common.exceptions.NoSuchElementException:
            print("找不到数据")
            return False
    def operate_element(self,  mOperate):
        print(mOperate)
        if self.findElement(mOperate):
            elements = {
                common.CLICK: lambda: operate_click(mOperate, self.driver),
                common.SEND_KEYS: lambda: send_keys(mOperate, self.driver),
            }
            return elements[mOperate["operate_type"]]()
        return False
# 点击事件
def operate_click(mOperate,cts):
    if mOperate["find_type"] == common.find_element_by_id or mOperate["find_type"] == common.find_element_by_name or mOperate["find_type"] == common.find_element_by_xpath:
        elements_by(mOperate, cts).click()
    if mOperate["find_type"] == common.find_elements_by_id or mOperate["find_type"] == common.find_elements_by_name:
        elements_by(mOperate, cts)[mOperate["index"]].click()
def send_keys(mOperate,cts):
    elements_by(mOperate, cts).send_keys(mOperate["text"])
# 封装常用的标签
def elements_by(mOperate, cts):
    elements = {
        common.find_element_by_id : lambda :cts.find_element_by_id(mOperate["element_info"]),
        common.find_elements_by_id : lambda :cts.find_elements_by_id(mOperate["element_info"]),
        common.find_element_by_xpath: lambda :cts.find_element_by_xpath(mOperate["element_info"]),
        common.find_element_by_name: lambda :cts.find_element_by_name(mOperate['name']),
        common.find_elements_by_name: lambda :cts.find_elements_by_name(mOperate['name'])[mOperate['index']],
        common.find_element_by_class_name: lambda :cts.find_element_by_class_name(mOperate['element_info']),
        common.find_elements_by_class_name: lambda :cts.find_elements_by_class_name(mOperate['element_info'])[mOperate['index']]
    }
    return elements[mOperate["find_type"]]()
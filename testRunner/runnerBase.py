__author__ = 'shikun'
# -*- coding: utf-8 -*-
import unittest
from common import operateYaml
import os
from selenium import webdriver as web


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)



def selenium_testcase():
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = web.Chrome(chromedriver)
    # driver = web.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
    driver.maximize_window()  #将浏览器最大化
    openurl = operateYaml.getYam(PATH("../open.yaml"))["openurl"]
    driver.get(openurl)
    return driver
class TestInterfaceCase(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(TestInterfaceCase, self).__init__(methodName)
    @staticmethod
    def setUpClass():
            pass
    def setUp(self):
        self.driver = selenium_testcase()
    def tearDown(self):

        pass
    @staticmethod
    def tearDownClass():
        print('tearDownClass')
    @staticmethod
    def parametrize(testcase_klass):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name))
        return suite


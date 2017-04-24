__author__ = 'shikun'
import os
from common import webCase
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
from testRunner.runnerBase import TestInterfaceCase
class testSetting(TestInterfaceCase):
    def setUp(self, methodName=''):
        super(testSetting, self).setUp()
        self.bc = webCase.WebCaseBase(driver=self.driver, casename="testSetting")
    def tearDown(self):
        self.driver.quit()
        pass
    def test_setting(self):
        self.bc.execCase(PATH("../yaml/setting.yaml"))


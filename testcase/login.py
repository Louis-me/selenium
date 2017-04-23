__author__ = 'shikun'
import os
from common import webCase
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

from testRunner.runnerBase import TestInterfaceCase
class testLogin(TestInterfaceCase):
    def setUp(self, methodName=''):
        super(testLogin, self).setUp()
        self.bc = webCase.WebCaseBase(driver=self.driver)
    def tearDown(self):
        self.driver.quit()
        pass

    def test_login(self):
        self.bc.execCase(PATH("../yaml/login.yaml"))


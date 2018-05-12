from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.Home.LoginPage import LoginPage
from PageObject.Home.LoginFailPage import LoginFailPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class HomeTest(ParametrizedTestCase):
    def testALoginFail(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/home/LoginFail.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = LoginFailPage(app)
        page.operate()
        page.checkPoint()

    def testBLogin(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/home/Login.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = LoginPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(HomeTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(HomeTest, cls).tearDownClass()

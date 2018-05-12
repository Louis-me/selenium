from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.My.HotTopicPage import HotTopicPage
from PageObject.Home.LoginPage import LoginPage
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class MyTest(ParametrizedTestCase):
    def login(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/home/Login.yaml"),
               "caseName": sys._getframe().f_code.co_name}
        page = LoginPage(app)
        page.operate()

    def testHotTopic(self):
        self.login()
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/my/HotTopic.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = HotTopicPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(MyTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(MyTest, cls).tearDownClass()

from Base.BaseRunner import ParametrizedTestCase
import os
import sys
from PageObject.cnblogs.AspNetPage import AspNetPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CnblogsTest(ParametrizedTestCase):
    def testAspNet(self):
        app = {"logTest": self.logTest, "driver": self.driver, "path": PATH("../Yamls/cnblogs/AspNet.yaml"),
               "caseName": sys._getframe().f_code.co_name}

        page = AspNetPage(app)
        page.operate()
        page.checkPoint()

    @classmethod
    def setUpClass(cls):
        super(CnblogsTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(CnblogsTest, cls).tearDownClass()

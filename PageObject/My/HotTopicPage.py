from PageObject import Pages
from Base.BaseYaml import getYam

'''
热门话题
'''


class HotTopicPage:
    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "test_msg": getYam(kwargs["path"]),
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass

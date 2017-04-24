__author__ = 'shikun'
import yaml
# -*- coding:utf-8 -*-
import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def getYam(homeyaml):
    try:
        with open(homeyaml, encoding='utf-8') as f:
            x = yaml.load(f)
            # print(x)
            return x
    except FileNotFoundError:
        print(u"找不到文件")


if __name__=="__main__":
    # x = getYam(PATH("../yaml/login.yaml"))
    # print(x["testinfo"])
    t=  [{'reason': '无法找到检查点', 'casename': 'testLogin', 'intr': '登录功能', 'id': 'test001', 'result': '失败', 'moudle': '登录',
      'test_img': 'D:\\app\\selenium\\log\\20170424155611\\登录功能CheckPoint_2_NG.png'},
     {'reason': '无法找到检查点', 'casename': 'testSetting', 'intr': '设置', 'id': 'test002', 'result': '失败', 'moudle': '登录',
      'test_img': 'D:\\app\\selenium\\log\\20170424155611\\设置CheckPoint_3_NG.png'}]
    for i in t:
        for k in i:
            print(i["reason"])
            break


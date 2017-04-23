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
    x = getYam(PATH("../yaml/login.yaml"))
    for key in x["check"]:
        print(key)

from Base.BaseStatistics import countInfo, countSum


def statistics_result(**kwargs):
    countInfo(result=kwargs["result"], testInfo=kwargs["testInfo"], caseName=kwargs["caseName"], name="chrome",
              driver=kwargs["driver"], logTest=kwargs["logTest"], testCase=kwargs["testCase"],
              testCheck=kwargs["testCheck"])
    countSum(kwargs["result"])


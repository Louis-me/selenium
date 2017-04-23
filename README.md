# 项目名及简介
* 此项目是在[Selenium](https://github.com/SeleniumHQ/selenium)开源工具封装而成的自动化和web测试工具

# 功能
* 都是基于python3
* 都是基于webdriver，大部分代码都可以通用，只是配置文件不一样
* 数据维护用的YMAL
* 邮件发送excel的测试报告


# 用法

**下载项目:**

```
git clone git@github.com:Louis-me/selenium_auto.git
```

**配置openurl.yaml**

```
openurl: http://www....com/login
```

**配置用例yaml**


```
testinfo: 
    - id: 001
      moudle: mok模块
      intr: 个人
testcase:
    - element_info: //*[@id="login"]/div[1]/div[2]/form/div[1]/input
      find_type: by_xpath
      operate_type: send_keys
      text: test
    - element_info: //*[@id="login"]/div[1]/div[2]/form/div[2]/input
      find_type: by_xpath
      operate_type: send_keys
      text: 123456
    - element_info: //*[@id="login"]/div[1]/div[2]/form/button[1]
      find_type: by_xpath
      operate_type: click
check:
    - element_info: //*[@id="home"]/a
      find_type: by_xpath

```



**命名行运行:**

```
pyhton testRunner/runner.py
```








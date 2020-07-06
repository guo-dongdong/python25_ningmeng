#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-01 15:30
# @Author  : guoDD
# @Email   : Email
# @File    : run_test

"""

"""
import os
import unittest
from datetime import datetime
import time

from class_06_单元测试.HTMLTestRunnerNew import HTMLTestRunner
from class_06_单元测试.test_cases import test_login, test_fut_login

# 收集测试用例
# 放到测试集合（测试套件）testsuite

# 1.初始化testloader
# 2.suite= testloader.discover(文件夹路径，‘demo_*.py)  发现测试用例
# 3.如果你想运行用例，要放到指定的文件夹当中
from class_06_单元测试.test_cases.test_login import TestLogin
from class_06_单元测试.test_cases.test_register import TestRegister

testloader = unittest.TestLoader()


# 查找测试用例，加载
dir_path = os.path.dirname(os.path.abspath(__file__))
case_path = os.path.join(dir_path, "test_cases")

suite = testloader.discover(case_path, 'test_*.py')

"""加载指定的模块(某一个)"""
# suite = testloader.loadTestsFromModule(test_login)

"""加载两个模块"""
# 加载两个测试套件，保存到测试套件中
# suite = testloader.loadTestsFromModule(test_login)
# suite2 = testloader.loadTestsFromModule(test_fut_login)
# # 将这两个测试套件合并添加到一个总的测试套件中
# suite_total = unittest.TestSuite()
# suite_total.addTests(suite)
# suite_total.addTests(suite2)

"""添加指定的测试类"""
# suite = testloader.loadTestsFromTestCase(TestLogin)
# suite2 = testloader.loadTestsFromTestCase(TestRegister)
# # 将这两个测试套件合并添加到一个总的测试套件中
# suite_total = unittest.TestSuite()
# suite_total.addTests(suite)
# suite_total.addTests(suite2)


"""添加摸一个方法（测试用例）"""
# 1.pychram 在方法名上右击运行







# #report
# report_path = os.path.join(dir_path, 'report')
# if not os.path.exists(report_path):
#     os.mkdir(report_path)
# file_path = os.path.join(report_path,'test_result.txt')
# # text
# with open(file_path, 'w', encoding='utf-8') as f:
#     # 初始化运行器，是以普通文本生成测试报告TextTestRunner
#     runner = unittest.TextTestRunner(f,verbosity=2)
#     runner.run(suite)
#     # runner.run(suite_total)

"""HTMLTestRunner"""
# HTMLTestRunner不是unittest自带的，需要自己去安装
# 安装不是通过pip，是别人写好的一个模块，你可以直接下载下来  .py
# 复制到项目目录下，然后导入
# 第二种方式，可以放到python的公共库当中

#report
report_path = os.path.join(dir_path, 'report')
if not os.path.exists(report_path):
    os.mkdir(report_path)

# 报告名称加时间戳
ts = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# ts = str(int(time.time()))
file_name = 'Test_Result_{}.html'.format(ts)

file_path = os.path.join(report_path,file_name)
# HTML
# TODO:HTML一定要使用二进制的方式打开
with open(file_path, 'wb',) as f:
    # 初始化运行器，是以普通文本生成测试报告HTMLTestRunner
    runner = HTMLTestRunner(f, title="我的第一份测试报告", description="真的第一份", tester="_小川")
    runner.run(suite)




"""
总结：
几种加载测试用例的方式
1.用的最多，整个项目一起加载，使用：discover
2.只加载一个具体的模块，使用：loadTestsFromTestCase
3.只加载一条用例，使用：loadTestsFromTestCase

"""

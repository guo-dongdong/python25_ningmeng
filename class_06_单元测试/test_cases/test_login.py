#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-30 15:17
# @Author  : guoDD
# @Email   : Email
# @File    : test_login

"""
1.模块名：以test开头
2.类以Test开头
"""

# 运行  -->右击出现“run 'unittest'” in ..
# 如果没有出现，那么要配置

import unittest
from class_06_单元测试.demo_01_unittest import visit




login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
login_data = {
    "mobilephone":"18300000001",
    "pwd":"12345678"
}
data = {"login_url":"http://test.lemonban.com/futureloan/mvc/api/member/login",
        "login_data":{"mobilephone":"18300000001","pwd":"12345678"}
        }

class TestLogin(unittest.TestCase):

    # 前置条件
    # 每一个测试用例方法执行之前都会运行的代码
    # setup
    # 可以吧测试数据放到setup当中
    def setUp(self) -> None:
        print("正在准备测试用例")
        self.data =data


    # tearDown:每次用例执行之后都会执行的方法。后置条件
    # 过程：
    def tearDown(self) -> None:
        print("测试用例执行完毕")


    def test_login_01_success(self):
        print("执行测试用例1")
        # 登录
        res = visit(login_url,login_data)
        print(res)

        # AssertionError
        try:
            self.assertEqual(1,3-2)
            # 1 / 0
        except AssertionError as e:
            # 如果你想断言失败，那么一定要抛出一个AssertionError
            print("断言失败", e)
            raise AssertionError

    def test_login_02_error(self):
        print("执行测试用例2")
        self.assertEqual(1,1)

    def test_login_03_demo(self):
        print("test_login_03_demo")

# 好习惯：写完代码空一行
# 如何运行：右击出现unittest



# 运行2.使用python去运行

# 断言结果：
# 1  . 表示通过，或者pass
# 2  F False ,表示断言没有通过
# 3  E Error ,表示程序内部发生了错误



if __name__ == '__main__':
    unittest.main()
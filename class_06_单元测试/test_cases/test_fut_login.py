#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-01 16:30
# @Author  : guoDD
# @Email   : Email
# @File    : test_fut_login

"""
	
"""
import unittest
from class_06_单元测试.demo_01_unittest import visit

url = "http://120.78.128.25:8766/futureloan/member/login"
headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
data1 = {"mobile_phone":"18111111111","pwd":"12345678"}
data2 = {"mobile_phone":"1812","pwd":"12"}
data3 = {"mobile_phone":"18122220000","pwd":"1234"}

class TestLoginFut(unittest.TestCase):

    def test_login_01_success(self):
        print("执行test_login_01_success")
        res = visit(url,json=data1,headers=headers)
        self.assertEqual(res["code"],0)
        print(res["msg"])



    def test_login_02_error_pwdError(self):
        print("执行test_login_02_error")
        res = visit(url, json=data2, headers=headers)
        self.assertEqual(res["code"], 2)
        print(res["msg"])

    def test_login_03_phoneError(self):
        print("test_login_03_phoneError")
        res = visit(url, json=data3, headers=headers)
        self.assertEqual(res["code"], 1001)
        print(res["msg"])



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-30 14:54
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_unittest

"""

1.单元测试框架：unittest
2.什么是单元测试：函数，类
3.单元测试谁去测，开发测试
4.单元测试框架和接口测试的关系

5.断言
判断预期结果和实际结果是否相等
assert

"""

# 访问接口
import requests

# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# login_data = {
#     "mobilephone":"18300000001",
#     "pwd":"12345678"
# }

def visit(url, data=None, json=None, **kwargs):

    login_res = requests.post(url, data=data, json=json, **kwargs)
    return login_res.json()


# url = "http://120.78.128.25:8766/futureloan/member/login"
# headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
# data1 = {"mobile_phone":"18111111111","pwd":"12345678"}
#
# # res = requests.post(url,json=data1, headers=headers)
# # print(res.json())
#
# print(visit(url,json=data1,headers=headers))

# print(visit(login_url,login_data))

# # 断言1+1==2
# assert 1+1 == 22
# print("assert finished")
#
# # 断言，如果断言失败，抛出异常
# # 如果成功



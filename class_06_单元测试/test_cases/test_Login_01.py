#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-04 13:02
# @Author  : guoDD
# @Email   : Email
# @File    : test_Login_01

import unittest


# import ddt
from class_06_单元测试.libs import ddt
from class_06_单元测试.common.excel_handler import ExcelHandler
from class_06_单元测试.common.requests_handler import RequestsHandler

# test_data = [
#     {"url":"http://120.78.128.25:8766/futuerloan/member/login",
#      "method":"post",
#      "headers":{"X-Lemonban-Media-Type":"lemonban.v2"},
#      "data":{"mobile_phone":"18111111111","pwd":"12345678"},
#      "expected":"hello world"},
# {"url":"http://120.78.128.25:8766/futuerloan/member/login",
#      "method":"post",
#      "headers":{"X-Lemonban-Media-Type":"lemonban.v2"},
#      "data":{"mobile_phone":"1811","pwd":"123"},
#      "expected" : "hello world"}
# ]
test_data = ExcelHandler(r'e:\test.xlsx').read("login")



@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    # def test_login_success(self):
    #     """测试用例通过"""
    #     data = tset_data[0]
    #     res = RequestsHandler().visit(data['method'],
    #                                   data['url'],
    #                                   data['method'],
    #                                   json=data['data'],
    #                                   headers=data['headers'])
    #     self.assertEqual(res, data['expected'])
    #
    #
    # def test_login_error(self):
    #     """不通过"""
    #     data = tset_data[1]
    #     res = RequestsHandler().visit(data['method'],
    #                                   data['url'],
    #                                   data['method'],
    #                                   json=data['data'],
    #                                   headers=data['headers'])
    #     self.assertEqual(res, data['expected'])

    @ddt.data(*test_data)
    def test_login(self, data):
        # 将 *test_data 当中的一组数据赋值到data这个参数

        res = RequestsHandler().visit(data['method'],
                                      data['url'],
                                      data['method'],
                                      json=eval(data['data']),
                                      headers=eval(data['headers']))

        self.assertEqual(res, data['expected'])


if __name__ == '__main__':
    unittest.main()



# ddt  ==》data driven testing
# 现在所说的是一个叫ddt的python库
# ddt库是和unittest搭配起来使用的，是unittest的一个插件
# python+unittest+ddt自动化测试框架

"""
@ddt.ddt
class TestDemo:

    @ddt.data()
    def test_demo(self):
        pass
"""
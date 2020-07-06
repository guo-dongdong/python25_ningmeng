#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-30 16:40
# @Author  : guoDD
# @Email   : Email
# @File    : test_assert

"""

unittest常用的断言方法

1.assertEqual(self, first, second, msg=None)

--判断两个参数相等：first == second

2.assertNotEqual(self, first, second, msg=None)

--判断两个参数不相等：first ！= second

3.assertIn(self, member, container, msg=None)

--判断是字符串是否包含：member in container

4.assertNotIn(self, member, container, msg=None)

--判断是字符串是否不包含：member not in container

5.assertTrue(self, expr, msg=None)

--判断是否为真：expr is True

6.assertFalse(self, expr, msg=None)

--判断是否为假：expr is False

7.assertIsNone(self, obj, msg=None)

--判断是否为None：obj is None

8.assertIsNotNone(self, obj, msg=None)
--判断是否不为None：obj is not None


断言方式：

"""
import unittest

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        #
        expected = 2
        actual = 1
        # self.assertEqual(expected, actual)    #提示方式更加具体，会把预期结果和实际结果打印出来
        # self.assertTrue(expected == actual)     #复杂的条件判断，不够具体
        self.assertGreater(expected, actual)
if __name__ == '__main__':
    unittest.main()
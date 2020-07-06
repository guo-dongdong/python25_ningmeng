#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-26 20:35
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_error

"""
异常：程序无法按照预计结果正常进行
一旦程序报错，程序将停止运行


# 异常处理：
try:
    我要执行的可能出现错误的代码
    当没有出现错误，那么try会执行完成
    一旦出现错误，立即跳到except里面
except:
    出现异常后要运行的代码


"""
num1 = input("输入第一个数字：")
num2 = input("输入第二个数字：")

try:
    print("hello")
    print(num1 * num2)
    print("hello111")
except:
    # 异常捕获 catch，如果出现错误，就按我说的做
    print("这里有一个bug")
    try:
        1/0
    except:
        print("1不能除于0")
    print("finish")

print("程序还在执行吗？")
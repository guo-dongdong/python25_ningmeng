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
except 异常类型:            -->不加异常类型时，默认所有错误（语法错误除外）
    出现异常后要运行的代码


常见的错误类型：
ImportError:无法引入模块或包
IndexError：下标索引超出序列边界
NameError：使用一个还未赋值对象的变量
SyntaxError：代码逻辑语法错误，不能执行；不能去捕获
TypeError：传入的对象类型与要求不符
ValueError：传入一个不被期望的值，即使类型正确
KeyError：试图访问字典中不存在的键
IOError：输入输出异常。文件操作


"""
num1 = input("输入第一个数字：")
num2 = input("输入第二个数字：")

try:
    print("hello")
    print(num1 * num2)
    print("hello111")
except IndexError:
    print("index error")
except Exception as err:
    # 异常捕获 catch，如果出现错误，就按我说的做
    print("这里有一个bug\n", err)
    print("finish")

    # 下面抛出一个异常：我要告诉程序，抛一个错误，终止这个程序
    raise NameError

finally:
    # 不管有没有异常，这里的代码都会执行
    print("不管有没有异常，都执行这句！")

print("程序还在执行吗？")



# def add(a,b):
#     if not isinstance(a,int):
#         raise ValueError
#     return a+b
#
# print(add("a",4))



# with
import os

dir_name = os.path.dirname(os.path.abspath(__file__))
guo = os.path.join(dir_name, "guodongdong.txt")
with open(guo,"w+",encoding='utf-8') as f:
    f.write("lanng")
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-27 16:57
# @Author  : guoDD
# @Email   : Email
# @File    : homeWork_01_class

"""
实现一个手机类，并实例你的手机
要求类里有：属性+行为。至少应该具有品牌，型号等信息，拨打电话，发送短信等功能
"""

# class Phone:
#
#     def __init__(self, pingpai, xinghao):
#         self.pingpai = pingpai
#         self.xinghao = xinghao
#
#     def call(self):
#         print("能打电话")
#
#     def SMS(self):
#         print("能发短信")
#
#
# xiaomi = Phone("xiaomi", "5s")
# xiaomi.call()
# xiaomi.SMS()
# print(xiaomi.pingpai)
# print(xiaomi.xinghao)

# 编写一个数学计算类，要求初始化方法带参数（两个数字），能够实现加减乘除运算（方法）
# class Calc(object):
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#
#     def addition(self):
#         return self.num1 + self.num2
#
#     def subtraction(self):
#         return self.num1 - self.num2
#
#     def multiplication(self):
#         return self.num1 * self.num2
#
#     def division(self):
#         try:
#             return self.num1 / self.num2
#         except ZeroDivisionError:
#             return "除数不能为零"
#
# calc = Calc(100,10)
# print(calc.addition())
# print(calc.subtraction())
# print(calc.multiplication())
# print(calc.division())


# 2.定义一个手机类，具有打电话和录音的功能，打电话的时候可以录音，可以不录音

class Mobile(object):
    # 如果不自己定义一个init，python会自动实现
    def __init__(self,model, color):
        self.color = color
        self.model = model

    def phone(self, record=True):
        if record == True:
            self.record()
        print("正在打电话")

    def record(self):
        print("{} 正在录音！".format(self))

    def __repr__(self):
        # 返回对象打印出来的效果，固定用法
        return self.model

modlie = Mobile("xiaomi5s","黑色")
# modlie.record()
modlie.phone(False)
modlie.phone()
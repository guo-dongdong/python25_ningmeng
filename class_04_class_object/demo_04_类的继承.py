#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-28 11:10
# @Author  : guoDD
# @Email   : Email
# @File    : demo_04_类的继承

"""
1.类的继承

-如何继承
    class 类名（父类名）：

-继承以后，子类可以使用父类的所有属性和方法

-如果父类和子类具有相同的方法和属性，子类会使用自己的方法和属性


"""


class Phone:

    recharge = True

    def call(self):
        print("打电话")

    def send_msg(self):
        print("发短信")


class SmartPhone(Phone):
    # def call(self):
    #     print("打电话")
    #
    # def send_msg(self):
    #     print("发短信")

    def call(self):
        self.caputure_video()
        print("智能手机——打电话")

    def caputure_video(self):
        print("视频")

smart = SmartPhone()
smart.call()
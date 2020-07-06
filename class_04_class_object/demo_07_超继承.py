#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-28 15:15
# @Author  : guoDD
# @Email   : Email
# @File    : demo_06_菱形问题


class Phone:

    recharge = True

    def call(self):
        print("phone打电话")


class SmartPhone(Phone):
    def call(self):
        # 完全重写
        self.caputure_video()
        # super()就是调用父类的call（）方法
        super().call()

    def caputure_video(self):
        print("SmartPhone视频")


smart = SmartPhone()

smart.call()
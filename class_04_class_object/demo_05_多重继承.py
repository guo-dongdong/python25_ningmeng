#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-28 11:23
# @Author  : guoDD
# @Email   : Email
# @File    : demo_05_多重继承

"""
1.多重继承
--子类可以同时继承多个父类，这些父类所有的特性（属性和方法），子类都可以使用

    class 子类名（父类1， 父类2， 父类3）：
        pass

类名：         类名（）：       类名（object）:---->都是一样的
--因为:所有的类都继承自object类。（所有类都是object的子类）

如果所有父类都有同一个方法，继承顺序的问题
--根据代码中继承的父类的先后顺序进行查找


"""
class MusicPlayer:
    def play(self):
        print("MP3播放音乐")

class GamePlayer:
    def play(self):
        print("游戏机正在玩游戏")

class Phone:

    recharge = True

    def call(self):
        print("打电话")

    def send_msg(self):
        print("发短信")

    def play(self):
        print("老年机正在下棋")


class SmartPhone(Phone, MusicPlayer, GamePlayer):
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

    # def play(self):
    #     print("只能手机正在玩")

smart = SmartPhone()

smart.play()
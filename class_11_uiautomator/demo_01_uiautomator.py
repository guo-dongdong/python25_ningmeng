#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-08-06 10:01
# @Author  : _小川_
# @Email   : Email@qq.com
# @File    : demo_01_uiautomator.py
from time import sleep

import uiautomator2 as u2

# 使用usb连接手机或模拟器，connect_usb是adb devices获取到的序列号
# 127.0.0.1:62001
# ERLDU19829003229
d = u2.connect('127.0.0.1:62001')
# d = u2.connect_adb_wifi('172.17.100.15')


# 得到设备的基本信息
# print(d.info)
# print(d.window_size())

# 启动APP
d.app_start('com.changhong.duiyu')
d.implicitly_wait(20)

# app信息
print(d.app_current())
# 元素定位-操作
d.xpath('//*[@resource-id="com.changhong.duiyu:id/btn_confirm"]').click()
sleep(10)

width, height = d.window_size()
for i in range(2):
    sleep(1)
    d.swipe(0.5*width, 0.9*height, 0.5*width, 0.1*height )


d.app_stop('com.changhong.duiyu')
d.app_clear('com.changhong.duiyu')
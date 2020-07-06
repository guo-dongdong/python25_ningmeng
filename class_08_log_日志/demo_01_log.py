#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 11:16
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_log

"""
log日志，记录

代码中日志的作用是记录信息，便于我们查看问题，定位问题
logging  标准库

日志级别
-1.NOSET   0    等于没写
-2.debug    10， 调试信息，一些额外信息，备注，往往和主体功能无关，日志里面的备注
-3.info     20   主体功能的信息。日志，做了什么
-4.warning  30  警告，下次可能要出错了
-5.error    40  错误
-6.critical 50  崩溃，及其严重

如何定义级别：
1.级别是我们自己定义的

"""
import logging


def old_function():
    try:
        1 / 0
        logging.info("代码没问题")
    except Exception as e:
        logging.error(e)
    logging.warning("这个方法再下一个版本中会抛弃,如果想正常使用，请用new_function")
    return "hello"

def new_function():
    return "new"


a = 1
b = 2
c = a+b

# 记录debug信息
logging.info("这只是一个普通的信息")
logging.debug("这是一个debug信息")
logging.warning("这是一个警告信息")
logging.error("出错了")
logging.critical("崩溃了")

if __name__ == '__main__':
    old_function()

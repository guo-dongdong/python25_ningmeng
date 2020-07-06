#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 11:43
# @Author  : guoDD
# @Email   : Email
# @File    : logging

"""
1.日志收集器：logger
2.日志收集器级别：level
3.日志处理器准备：handler
4.日志处理器级别设置：
5.logger.addHandler(handler)
6.设置日志格式：format
7.添加日志处理器,handler.setFormatter(fmt)

设置级别：
当设置为debug的时候，只有高于，等于该级别的才会打印出来


"""


import logging

# 初始化logger收集器
logger = logging.getLogger('python25')

# 设置收集器级别
logger.setLevel("WARNING")

# 笔的默认级别是warning,默认是使用控制台输出
# 放到一个file文件当中
handler = logging.FileHandler('log.txt')
handler.setLevel('DEBUG')

# 添加handler
logger.addHandler(handler)

# 设置格式
fmt = logging.Formatter('%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(fmt)

logger.info("hello_info")
logger.debug("hello")
logger.warning("world12ert")
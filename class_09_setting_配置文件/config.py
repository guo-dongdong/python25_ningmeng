#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 17:37
# @Author  : guoDD
# @Email   : Email
# @File    : config

"""
存储配置项
"""
import sys

#
# logger_name = 'python25'
# logger_file = 'python25_log.txt'

class LoggerConfig:
    logger_name = 'python25'
    logger_file = 'python25_log.txt'
    level = 'DEBUG'

class ProductLoggerConfig(LoggerConfig):
    level = 'WARNING'

# if sys.platform == 'linux':
#     config = ProductLoggerConfig
# else:
#     config = LoggerConfig
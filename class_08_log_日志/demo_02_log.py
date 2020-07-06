#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 17:01
# @Author  : guoDD
# @Email   : Email
# @File    : demo_02_log

"""

"""
from class_08_log_日志.logger_handler_02 import logger

def main():
    print('hello')
    logger.info('hello')

def hello():
    logger.error("hello")

if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 17:28
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_配置文件

"""
配置：
变量，随时都会变化的
常量：一般来说，你的成语启动以后，几乎不会发生变化的数据

python的配置文件形式：
1.通过python模块 ---  .py文件作为配置的文件
2.yaml文件   ---   。yaml/.yml
3. ---   .ini    .conf   .xml文件
"""

from class_08_log_日志.logger_handler_02 import logger

def main():
    print('hello')
    logger.info('hello')

def hello():
    logger.error("hello")

if __name__ == '__main__':
    main()
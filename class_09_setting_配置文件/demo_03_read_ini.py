#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 18:25
# @Author  : guoDD
# @Email   : Email
# @File    : demo_03_read_ini

"""
读取ini
"""

from configparser import ConfigParser

# 初始化
config = ConfigParser()

# 读取
config.read('python_25.ini', encoding='utf-8')

a = config.get('teachers','name')
print(a)
print(type(a))
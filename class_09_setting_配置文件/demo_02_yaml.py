#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-07-05 17:50
# @Author  : guoDD
# @Email   : Email
# @File    : demo_02_yaml

"""
读取yaml

pip install pyyaml
"""
import yaml

# 读取yaml配置文件,加载配置项
# f = open('python_25.yaml')
# data = yaml.load(f.read(),Loader=yaml.FullLoader)
#
# print(data)
# f.close()

with open('python_25.yaml', encoding='utf-8') as f:
    data = yaml.load(f.read(), Loader=yaml.FullLoader)
print(data['logger']['name'])

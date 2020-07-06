#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-26 18:23
# @Author  : guoDD
# @Email   : Email
# @File    : demo_04_OS

# 内置模块os
# os 主要处理系统相关的
# os.path 主要处理系统路径相关的

import os.path
print(os.getcwd())   #类似linux中的pwd,显示当前文件路径

print(os.path.abspath(__file__))        #绝对路径

print(os.path.dirname(os.path.abspath(__file__)))        # 获取文件的文件夹名称，dirname


# 路径拼接 os.path.join()
a = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(a, "guodongdong"))


# 创建目录 os.mkdir  不能创建多层，一次只能建一级
data_path = os.path.join(a, "data")
# os.mkdir(data_path)

# 删除目录
# os.rmdir(data_path)

#是否是一个文件夹
print(os.path.isdir(data_path))
#是否是一个文件
print(os.path.isfile(data_path))

# 路径是否真的存在
print(os.path.exists(data_path))
guodongdong = os.path.join(a, "guodongdong")
print(os.path.exists(guodongdong))

# 判断data是否存在，存在pass，不存在创建
if not os.path.exists(guodongdong):
    os.mkdir(guodongdong)


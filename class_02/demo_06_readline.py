#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-26 20:23
# @Author  : guoDD
# @Email   : Email
# @File    : demo_06_readline

import os

dir_name = os.path.dirname(os.path.abspath(__file__))
guo = os.path.join(dir_name, "guodongdong.txt")

f = open(guo, encoding='utf-8')

# 只读取一行
print(f.readline())

#读取多行 readlines() --得到的是一个列表
a = f.readlines()
for i in a:
    print(i, end="")
f.close()
"""
读取的机制：根据光标移动的
"""
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-26 19:42
# @Author  : guoDD
# @Email   : Email
# @File    : demo_05_open

"""
os和open的作用：
"""

# 如何读取文件
# 1.打开文件。open()
# 2.读取
# 3.关闭文件

# open(path/文件名称，mode='r',encoding='utf-8')
# mode:
# 1."r",读取
# 2."w",写入（覆盖）;"a",追加写入
# 3."b",bindry,二进制
# 4."t",文件模式，字符串模式

import os

dir_name = os.path.dirname(os.path.abspath(__file__))
guo = os.path.join(dir_name, "guodongdong.txt")

'''读取文件'''
# # 打开
# f = open(guo,encoding="utf-8")
# # # 读取
# print(f.read())
# # 关闭文件
# f.close()
#
# # 编码：string  -->  byte
# # 解码：byte  -->  string
#
# print("hello".encode())
# print(b'hello'.decode())

'''写入文件'''
f = open(guo,mode='a' , encoding='utf-8')
f.write("hello world!!!!!!!!!!!!!!!!!!!!!!!")
f.close()

png = os.path.join(dir_name,'1.png')
f_1 = open(png,mode='rb')
print(f_1.read())
f_1.close()
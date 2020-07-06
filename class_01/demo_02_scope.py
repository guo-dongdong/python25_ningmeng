#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-26 10:04
# @Author  : guoDD
# @Email   : Email
# @File    : demo_02_scope


'''
1.函数体内定义的变量，叫局部变量。局部变量只能在函数体里面生效
2.函数体外定义的变量，叫全局变量。全局变量在函数体里面和外面都能生效
3.函数的参数是局部变量
4.局部变量能在函数体里面被修改，不能再函数体外面被修改
5.全局变量不能在函数体里面修改(可以在函数体中使用global声明变量，再进行修改（不建议使用）)，能够在函数体外面修改
6.global---全局变量声明，强烈不建议使用
'''


name = "guodd"

def dl():
    # name = "123"
    global name
    name = name + "1234567890"
    print("{} is dl".format(name))
dl()
print(name)
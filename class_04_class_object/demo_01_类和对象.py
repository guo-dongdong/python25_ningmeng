#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-27 15:06
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_类和对象

"""
1.什么是类？
具有相同特征的一些事务的种类，集合

class 类名（）：
    类的内容
    类体

类名：也是标识符，符合标识符的规范------字母、数字、下划线，且不能以数字开头
-不能是关键字
-大驼峰式命名   BigBoss

类的使用：类的实例化，对象化，初始化
可以使用整个类

2.什么是对象？
对象就是类当中的一个成员，TODO:如何表示某一个成员


"""


class BigBoss:
    pass

print(BigBoss)          # -->使用整个类，
print(BigBoss())        # -->使用类当中的一个成员     TODO:对象，实例，object
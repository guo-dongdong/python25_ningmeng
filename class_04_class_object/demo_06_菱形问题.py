#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-28 15:15
# @Author  : guoDD
# @Email   : Email
# @File    : demo_06_菱形问题

"""
广度优先
深度优先

# 查找顺序
print(D.__mro__)



"""


class A:
    def play(self):
        print("A is playing")

class B(A):
    # def play(self):
    #     print("B is playing")
    pass

class C(A):
    def play(self):
        print("C is playing")

class D(B,C):
    # def play(self):
    #     print("D is playing")
    pass

d = D()
d.play()
# 查找顺序
print(D.__mro__)
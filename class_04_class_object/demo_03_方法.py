#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-27 21:00
# @Author  : guoDD
# @Email   : Email
# @File    : demo_03_方法
"""
1.什么是方法
--类里面的函数，就叫做方法

函数和方法：

方法和属性的关系：
--属性：特征，名词
--方法：行为，动作，动词

方法和方法之间的相互调用---> self.方法名（参数）

--带有self参数的方法叫做实例方法
--self可以修改，self只是用来占位的。但是强烈不建议修改

没有self的方法：
--1.静态方法
--就是表示刚刚好放在类下面的普通的函数
    # 声明静态方法
    @staticmethod
--只是为了方便管理我们的代码

静态方法的调用： self.方法（）   obj.方法（）
类名.方法名

类方法：
--cls：表示类本身
--类方法的定义：
    # 声明类方法
    @classmethod

类方法的调用：
--类.方法名（）
--实例.方法名（）

类方法：主要用来做备用的构造函数
实例方法：用的最多
静态方法：有提示的时候


"""
# def demo_02(food_01):
#     return "喜欢吃 {} ".format(food_01)

class Demo:

    favor = "python"

    def __init__(self, name):
        self.name = name

    # 声明静态方法
    @staticmethod
    def eat(food):
        print("喜欢吃 {} ".format(food))
        return "喜欢吃 {} ".format(food)

    def offer(self, money, food):
        print("恭喜{} 拿到 {} 的offer".format(self.name,money))
        food = self.eat(food)


    # 声明类方法
    @classmethod
    def code(cls):
        print("我喜欢的编程语言是 {} ".format(cls.favor))
        demo1 = Demo("guo")
        demo1.offer("30k", "牛肉面")

    @classmethod
    def make_instance(cls, name):
        return cls(name)


demo = Demo("guodongdong")
demo.offer("40K","辣条")
demo.eat("辣条")
Demo.eat("方便面")


"""
总结：
1.方法：
什么是方法--类下面的函数，表示类或者对象的行为

静态方法：
实例方法：
类方法：

方法和方法之间的调用---和普通函数差不多：前面要加前缀，
"""

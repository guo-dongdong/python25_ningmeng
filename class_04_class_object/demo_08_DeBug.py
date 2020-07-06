#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-28 15:46
# @Author  : guoDD
# @Email   : Email
# @File    : demo_08_DeBug

"""
1.debug
调试：
-1，最简单的方式，print()，缺陷：1.print（a）,2.调试完还要删除
-2.出问题，先print百度
-3.断点

如何使用debug模式：
1.小虫子的标记，断点配合起来使用
2.断点：程序运行到红点的地方，会暂停

step over f8：下一行，单步调试
resume program：下一个断点
run to cursor:运行到指定行，光标处
setp into:进入对应的代码
setp into my code:进入


"""
class Phone:

    recharge = True

    def call(self):
        print("phone打电话")


class SmartPhone(Phone):

    def __init__(self,brand):
        self.brand = brand

    def call(self):
        # 完全重写
        a = 4
        print(a)
        self.caputure_video()
        # super()就是调用父类的call（）方法
        super().call()

    def caputure_video(self):
        print("SmartPhone视频")


smart = SmartPhone("xiaomi")

smart.call()

print(getattr(smart,"brand","华为"))
print(getattr(smart,"brand_01","华为"))

phone = SmartPhone("apple")
phone.brand = "xiaomi"
print(phone.brand)

phone.color = "red"
print(phone.color)

# 获取属性如果不存在，会报错；
# 修改属性如果不存在，会直接赋值
setattr(phone,"food","辣条")
print(phone.food)
setattr(phone,"brand","poop")
print(phone.brand)


"""

总结：
1.继承：子类要使用父类的属性或方法
2.多重继承：一个类同时继承多个父类，可以同时使用多个父类中的属性和方法
--多个类同时有某个方法，调用顺序（菱形问题）
3.super（）
4.debug模式

getattr：获取属性（动态获取某个属性的函数）
getattr(对象或者类名，属性名称，当没有此属性的时候，需要提供的默认值)

# 获取属性如果不存在，会报错；
# 修改属性如果不存在，会直接赋值

有时候，我们提前不知道属性名称是什么，是从别的地方拿来的
-setattr：设置属性
-setattr(对象或者类名，属性名称，赋值的新值)
--不管属性存不存在，都会赋值

"""
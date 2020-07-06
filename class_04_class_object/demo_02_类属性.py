#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-27 15:32
# @Author  : guoDD
# @Email   : Email
# @File    : demo_02_类属性

"""
1.类的属性：包括类属性和实例属性
2.类属性：类集体的属性

属性：成员都具备的特征
--类里面表示的变量，就是属性
--类属性又称为类变量

3.类属性获取：
--类名.属性名
--实例名.属性名

4.类属性的修改：
--类名.属性名 = "新值"

5.实例属性（实例变量）：表示类成员自己独有的特征，并不是每个类成员都具备的

如何定义一个具体的对象
--集体的对象的定义，会在类的下面定义一个固定的函数名称：__init__()
    def __init__(self):
        pass

如何使用对象，初始化对象
--初始化对象的时候：类名（参数1，参数2，。。。）
--初始化对象定义的时候：__init__(seif,参数1，参数2，。。。)

总结：具体对象使用的时候 实际上是调用__init__函数

-如何表示实例属性
-实例属性的定义：__init__里面：seif.属性名 = 属性值
-实例属性的使用：实例名称（不是类名）.属性名
-实例属性的修改：实例名称.属性名 = 新值

self:是在类的定义当中，表示实例对象自己。

"""
class BigBoss:

    # 属性
    code_level = "very good"
    hair = "very thin"
    hobby = "zhai"

    def __init__(self,name, food, gender):
        """表示定义具体的对象，初始化函数，初始化方法"""
        print(name)
        print(food)
        print(gender)
        self.dalao_name = name
        self.food = food
        self.gender = gender

    def hello_world(self):
        """实例方法"""
        print(self.dalao_name, "哭。。。。。。。。。。。。")
        return "哭是正常的！！"

    pass

# 获取类属性
print(BigBoss.code_level)
print(BigBoss.hair)

BigBoss.hobby = 'party'
print(BigBoss.hobby)

# 初始化对象，实例化
baby = BigBoss("guodongdong","牛肉面","男")
print(baby.code_level)

# 获取实例属性
print(baby.gender)

print(baby.hello_world())

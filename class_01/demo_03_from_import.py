#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-26 11:06
# @Author  : guoDD
# @Email   : Email
# @File    : demo_03_from_import


# 1.模块，moudle，就是一个py文件，一个模块里会有很多函数、类
# 2.包，package，就是一个py文件的文件夹，会有一个或多个模块
# 3.包包含一个 __init__.py模块
# 4.库，标准库，第三方库：实现特定功能的代码集合，可以是一个模块或一个包
# 5.模块导入的作用
# import关键字

'''
总结：
1.函数的相互调用（python代码内部执行的机制）
2.调用顺序
3.局部变量和全局变量
    获取：
    修改：
4.内置函数
5.模块和包
6.查看源码的方法：1.看函数名称 2.注解 3.返回值 4.参数
'''

# 查找模块的顺序：
# from (项目的根目录开始)包名.包名.包名.模块名 import 。。。（类名，函数名，变量名）

# 模块导入
# #1. from ...(模块名称) import ...（类名，函数名，变量名）  ---适用于项目根目录、内置模块
# from module_01 import run
# run()
#
# #2. from (项目的根目录开始)包名.包名.包名.模块名 import ...（类名，函数名，变量名）   ---适用于自己定义的
#
# from class_01.module_02 import run_01
# run_01()
#
# #3. from (项目的根目录开始)包名.包名.包名 import ...(模块名)
# from class_01 import module_02
# module_02.run_01()
#
# #4. 如果出现了重名的函数，那么要使用as 别名；函数名很长的情况也可以使用as进行别名处理
# from class_01.module_02 import run_01 as r1
# r1()
#
# #5. import 模块名 （as ） ---只能导入模块名---更适合用在内置模块
# import time
# print(time.time())

"""
模块被导入时发生了什么？
把导入的模块中所以顶格的内容读取一遍
"""

'''
__file__        ：这么模块的路径
__name__        ：
    如果当前模块是用来作为程序运行的脚本文件（入口文件），那就是__main__；
    如果不是程序运行的脚本文件，是作为模块导入其他地方的，那就是包名.包名.模块名
__main__        :运行python文件的模块名
'''
from class_01 import module_02

print(__file__)
print(__name__)

if __name__ == '__main__':
    print("hello world main!")

'''
if __name__ == '__main__':
    pass
    
    # 当py文件被作为脚本（入口）执行的时候，if下面的代码会执行
    # 如果py文件是被导入其他的模块，if下面的代码不会执行
'''

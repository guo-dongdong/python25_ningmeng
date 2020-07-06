#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-23 18:41
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_fanc


# # 定义函数
# def add(x):
#     y = x+1
#     return y
# print(add(1))

# my_list = [1,2,3]
# my_list.append("hello")
# print(my_list)

#作业1
# while True:
#     a = int(input("请输入1-7的数字："))
#     if a == 0:
#         break
#     elif a >=1 and a<=5:
#         print("周{}".format(a))
#     elif a >=6 and a <=7:
#         print("周末")
#     else:
#         print("输入有误，请重新输入！")
#
# 列表去重
# a = [1,2,3,4,5,4,1,4]
# print(list(set(a)))
#
# new_a = []
# for i in a:
#     if i not in new_a:
#         new_a.append(i)
# print(new_a)

# 变量交换
# def variable_Exchange(a,b):
#     temp = a
#     a = b
#     b = temp
#     return a,b
#
# print(variable_Exchange(1,2))

#
# def DL(name,money,food):
#     print("ll {} abc {} edf".format(name,money))
#
# # 位置参数
# DL("guodd",10,"00")
#
# # 关键字参数
# DL(name="guodd",money=10,food="00")
#
# # 默认参数
#
# # 不定长参数
# def sum(a,b,*args,**kwargs):
#     '''*args接收剩下的位置参数'''
#     """**kwargs接收剩下的关键字参数"""
#     """*后面的名称可自定义，不是固定的"""
#
#
#
#     total = a +b
#     for i in args:
#         total += i
#     return total
#
# a = [3,4,5]
# print(sum(1,2,*a))


num_dict = {"1":"!","2":"@","3":"#","4":"$","5":"%","6":"^","7":"&","8":"*","9":"(","0":")"}
def num_return(num):
    if num in num_dict:
        return num_dict[num]

def num_input():
    a = int(input("请输入0-9的数字："))
    if a >= 0 and a <=9:
        print(num_return(str(a)))
    else:
        return "error"
num_input()

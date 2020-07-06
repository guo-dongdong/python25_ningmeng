#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-30 14:12
# @Author  : guoDD
# @Email   : Email
# @File    : demo_06_res_cookie

"""
cookies:

session:一个session就是一次会话对象
每开一次浏览器（session过期时间默认）
session（Jsession='9F2E731E88A2698632B7CA3EAEB9793A'）
"""
import requests
# 如何操作cookie


# # 前程贷url
# login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
# login_data = {
#     "mobilephone":"18300000001",
#     "pwd":"12345678"
# }
# login_res = requests.get(login_url,login_data)
# # print(res.json())
# # print(res.headers)
#
# # 获取cookie
# cookies = login_res.cookies
#
# # 充值
# recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
# recharge_data = {"mobilephone":"18300000001","amount":"1000"}
#
# resrecharge_res= requests.post(recharge_url,data=recharge_data,cookies=cookies)
# print(resrecharge_res.json())

# session
session = requests.Session()

login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
login_data = {
    "mobilephone":"18300000001",
    "pwd":"12345678"
}
login_res = session.post(login_url,login_data)

# 充值
recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {"mobilephone":"18300000001","amount":"1000"}

resrecharge_res= session.post(recharge_url,data=recharge_data)
print(resrecharge_res.text)
# 关闭session
session.close()

# 初始化另一个session
session_another = requests.Session()
res = session_another.post(recharge_url,data=recharge_data)
print(res.text)
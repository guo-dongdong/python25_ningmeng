#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-29 17:06
# @Author  : guoDD
# @Email   : Email
# @File    : demo_04_requests_post

"""

"""

import requests

# 发送post请求
# url = "http://www.baidu.com"
# res = requests.post(url)

# 发送请求头header
# headers = {"token":"123456","name":"guodong"}
# url = "http://www.baidu.com"
# res = requests.post(url,headers=headers)

# 传递参数
headers = {"token":"123456","name":"guodong"}
url = "http://www.baidu.com"
# query_string形式
# data = {"username":"test","admin":"admin"}
# res = requests.post(url,headers=headers,params=data)
# form表单形式
# form_data = {"user":"admin","pwd":"1234567890"}
# res = requests.post(url,data=form_data,headers=headers)

# json格式
json_data = {"json_data":"json"}
res = requests.post(url,json=json_data,headers=headers)

# json和form表单参数不可以同时传，但他们都可以和params（query_string）同时传递




"""获取响应数据"""
# print(res.text)
"""获取二进制形式"""
# print(res.content)
"""获取json"""  # 不是json格式的数据，会报错 try  except
print(res.json())
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-29 16:44
# @Author  : guoDD
# @Email   : Email
# @File    : demo_03_request

"""
第三方库：requests库

1.安装: pip install requests
2.使用 import requests


"""

import requests

# # 访问一个url接口地址

# # 发送一个get请求
# url = 'http://www.baidu.com'
# req = requests.get(url)
# print(req)

# # 如何添加一个请求头
# headers ={"token": "123456","username": "guodong"}
# url = 'http://www.baidu.com'
# res = requests.get(url,headers=headers)

# # 如何传递参数，位置参数，或者关键字参数params(query_string的形式传递)
# headers ={"token": "123456","username": "guodong"}
# url = 'http://www.baidu.com'
# data = {"username":"guodongdong","passwd": "12345678"}
# res = requests.get(url, params=data, headers=headers)


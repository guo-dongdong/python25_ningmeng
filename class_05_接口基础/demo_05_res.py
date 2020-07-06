#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-30 11:08
# @Author  : guoDD
# @Email   : Email
# @File    : demo_05_res

"""

"""

import requests

# 注册
register_url = "http://120.78.128.25:8766/futureloan/member/register"
# 登录
login_url = "http://120.78.128.25:8766/futureloan/member/login"
headers = {"X-Lemonban-Media-Type":"lemonban.v2"}
data = {"mobile_phone":"18300000001","pwd":"12345678"}

# 一定要添加headers 关键字参数，不能以位置参数传递
# 因为放到了可变长参数里面
# content-type参数不需要添加，json关键字参数就是表示content-type=application/json
# data关键字参数就是表示 表单格式
# params参数就是表示 query string

# 登录接口
# token可以放在请求体中？根据接口文档，只是一种协议，开发人员和你之间定义的协议
# cookie可以放在请求体中？不能，协议

res = requests.post(login_url,json=data,headers=headers)
# print(res.json())

# 充值
recharge_url = "http://120.78.128.25:8766/futureloan/member/recharge"
token = res.json()["data"]["token_info"]["token"]
id = res.json()["data"]["id"]
recharge_headers = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization":"Bearer {}".format(token)}
recharge_data = {"member_id":id,"amount":100}

res = requests.post(recharge_url,json=recharge_data,headers=recharge_headers)
print(res.json())

# 访问其他接口


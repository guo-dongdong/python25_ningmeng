#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @CreateTime    : 2020-06-28 18:30
# @Author  : guoDD
# @Email   : Email
# @File    : demo_01_接口

"""
1.什么是接口：
-前后端沟通的桥梁
-数据通道
我们所讲的接口概念：web api

API：应用程序可编程接口，全称（Application Programming Interface）

硬件接口
软件接口

run函数:可以被外部

http请求：
1.请求首行：请求的概要信息
2.请求头
3.请求体

请求首行包含的内容：
-请求网址，url
-请求方法
-远程地址
-状态码
-版本

面试题：列举出你会的请求方法
（1）GET方法：获取资源
（2）POST方法：传输实体主题
（3）PUT方法：传输文件
（4）HEAD方法：获取报文首部
（5）DELETE方法：删除文件
（6）OPTIONS方法：询问支持的方法

get和post的区别：
-get表示获取资源，post表示创建资源
-get没有请求体，post有请求体
-get请求参数（query string查询字符串）放在url中以？key=value&key1=value1的形式；post不仅可以查询字符串，而且可以放在请求体里面
-post比get更安全

请求头：
user-Agent：用户代理，客户端是什么
content-Type:请求数据格式
cookie：缓存中的其中一中机制

请求体：



响应：
1.响应首行（状态行）         --协议版本，响应状态码
2.响应头
3.响应体


响应首行：
-协议版本
-响应状态码

1.100-199信息响应
--100 Continue: 服务器通知浏览器之前一切正常，请客户端继续请求，如果请求结束，可忽略；
--101 Switching Protocal: 针对请求头的Upgrade返回的信息。表明服务器正在切换到指定的协议。
--103 Early Hints: 此状态代码主要用于与Link 链接头一起使用，以允许用户代理在服务器仍在准备响应时开始预加载资源

2.200-299成功响应
--200 OK： 请求成功
--201 Created: 常用于POST，PUT 请求，表明请求已经成功，并新建了一个资源。并在响应体中返回路径。
--202 Accepted: 请求已经接收到，但没有响应，稍后也不会返回一个异步请求结果。 该状态码适用于等待其他进程处理或者批处理的场景。
--203 No-Authoritative Information: 表明响应返回的元信息（meta-infomation）和最初的服务器不同，而是从本地或者第三方获取的。
--204 No Content: 请求没有数据返回，但是头信息有用。用户代理(浏览器)会更新缓存的头信息。
--205 Reset Content: 告诉用户代理（浏览器）重置发送该请求的文档。
--206 Partical Content: 当客户端使用Range请求头时，返回该状态码。

3.300-399重定向消息
--300 Multiple Choice： 返回多个响应，需要浏览器或者用户选择；
--301 Moved Permanently: 请求资源的URL被永久的改变，新的URL会在响应的Location中给出。
--302 Found:  请求资源的URL被暂时修改到Location提供的URL。未来可能还会有新的修改。
--303 See Other: 服务通过返回的响应数据指导客户端通过GET方法去另一个URL获取资源。
--304 Not Modified: 资源未变更。服务器根据请求头判断，需要资源未修改，只返回响应头；否则将资源一起返回
--307 Temporary Redirect: 临时重定向。基本和302相同。
--308 Permanent Redirect: 永久重定向。基本和301相同。但是严格禁止修改请求方式和请求体。

4. 400-499 客户端错误响应
--400 Bad Request: 请求语法有问题，服务器无法识别。
没有host请求头字段，或者设置了超过一个的host请求头字段。
--401 UnAuthorized: 客户端未授权该请求。缺乏有效的身份认证凭证，一般可能是未登陆。登陆后一般都解决问题。
--403 Forbidden: 服务器拒绝响应。权限不足。
--404 Not Found: URL无效或者URL有效但是没有资源。
--405 Method Not Allowed: 请求方式Method不允许。但是GET和HEAD属于强制方式，不能返回这个状态码。
--406 Not Acceptable: 资源类型不符合服务器要求。
--407 Proxy Authorization Required: 需要代理授权。
--408 Request Timeout：服务器将不再使用的连接关闭。响应头会有Connection: close。
--426 Upgrade Required: 告诉客户端需要升级通信协议。

5. 500-599 服务器错误响应
--500 Internal Server Error: 服务器内部错误，未捕获。
--502 Bad Gateway: 服务器作为网关使用时，收到上游服务器返回的无效响应。
--503 Service Unavailable: 无法服务。一般发生在因维护而停机或者服务过载。
一般还会伴随着返回一个响应头Retry-After: 说明恢复服务的估计时间。
--504 Gateway Timeout: 网关超时。服务器作为网关或者代理，不能及时从上游服务器获取响应返回给客户端。
--505 Http Version Not Supported: 发出的请求http版本服务器不支持。如果请求通过http2发送，服务器不支持http2.0，就会返回该状态码。

响应头：
-content-type：返回数据的格式
-set-cookie：

响应体：
-返回的数据










"""

def run():
    return "run"
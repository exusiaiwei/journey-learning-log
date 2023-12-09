# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
#from .myextend import pro
import random

class ProxyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    def process_request(self, request, spider):
        proxy = "w309.kdltps.com:15818"

        # 用户名密码认证(私密代理/独享代理)
        username = "t17784574602291"
        password = "qf8swpku"
        request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                        "proxy": proxy}

        # 白名单认证(私密代理/独享代理)
        #request.meta['proxy'] = "http://%(proxy)s/" % {"proxy": proxy}
        return None
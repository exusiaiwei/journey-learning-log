# encoding: utf-8


class IPProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = "w309.kdltps.com:15818"

        # 用户名密码认证(私密代理/独享代理)
        username = "t17784574602291"
        password = "qf8swpku"
        request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password,
                                                                        "proxy": proxy}

        #白名单认证(私密代理/独享代理)
        #request.meta['proxy'] = "http://%(proxy)s/" % {"proxy": proxy}
        return None

    #def process_request(self, request, spider):
    #    """
    #    将代理IP添加到request请求中
    #    """
        #proxy_data = self.process_request()
        #if proxy_data:
    #        current_proxy = f'http://{proxy_data}'
    #        spider.logger.debug(f"current proxy:{current_proxy}")
    #        request.meta['proxy'] = current_proxy

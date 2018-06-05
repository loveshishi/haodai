# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from scrapy.exceptions import NotConfigured
from scrapy.http import HtmlResponse
from selenium import webdriver

class RandomProxyMiddleware(object):
    def __init__(self,settings):

        self.max_failed = 3
        """
        setting.getlist("PROXIES")是获取setting
        中定义的PROXIES的内容
        """
        self.proxies = settings.getlist("PROXIES")

        """
        定义每个代理的失败次数，创建的是字典
        """
        self.stats = {}.fromkeys(self.proxies,0)

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('HTTPPROXY_ENABLED'):
            raise NotConfigured

        # 该语句执行的是同一个类中的init方法
        return cls(crawler.settings)

    def process_request(self,request,spider):
        if not 'proxy' in request.meta:
            request.meta['proxy'] = random.choice(self.proxies)
            print('-'*50,request.meta['proxy'])

    def process_responese(self,request,response,spider):
        cur_proxy = request.meta['proxy']
        if response.status >= 400:
            self.stats[cur_proxy] += 1
        if self.stats[cur_proxy] >= self.max_failed:
            if cur_proxy in self.proxies:
                self.proxies.remove(cur_proxy)
                print("delete %s from proxies list" % cur_proxy)
        return response

    # 代理出现问题后的
    def process_exception(self,request,exception,spider):
        cur_proxy = request.meta['proxy']
        print('raise exception:%s when use %s' % (exception,cur_proxy))
        if cur_proxy in self.proxies:
            self.proxies.remove(cur_proxy)
            print("delete %s from proxies list" % cur_proxy)
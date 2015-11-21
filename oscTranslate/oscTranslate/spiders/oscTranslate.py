# -*- coding: utf-8 -*-
__author__ = 'AllenCHM'

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import json
import pymongo
from scrapy import Request
import time
import re

class TranslateScrapy(BaseSpider):
    name = u'Translate'
    allowed_domains = [u'oschina.net', ]
    start_urls = [
        u'http://www.oschina.net/translate/list?type=2.com'
    ]

    # def __init__(self):
    #     self.connectionMongoDB = pymongo.MongoClient(host='192.168.2.165', port=27017)
    #     self.db = self.connectionMongoDB['bilibili']
    #     self.doc = self.db["avIndex"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        articles = hxs.xpath('//div[@class="article"]')
        for article in articles:
            href = article.xpath('.//dt/a/@href').extract()[0]
            title = article.xpath('.//dt/a/@title').extract()[0]
            downloadTime = time.time()

            print
    # def spider_close(self):
    #     self.connectionMongoDB.close()
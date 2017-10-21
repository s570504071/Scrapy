#-*-coding:utf-8-*-
import scrapy
from fortext.items import LlItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re


class LiuliSpider(CrawlSpider):
    name = 'll'
    allowed_domains = ['hacg.ch']
    start_urls = [
        'http://www.hacg.ch/wp/category/all/anime/page/1/'
    ]
    rules=(
        #对所有页面跟进并从每个分页中提取分支链接！
        Rule(LinkExtractor(allow=(r'http://www.hacg.ch/wp/category/all/anime/page/[0-9]*/',))  ,follow=True),
        #Rule(LinkExtractor(allow=(r'http://www.hacg.ch/wp/category/all/anime/page/[0-9]*/',)),callback='self.parse_gethtml', follow=True),
        #有不同，没有category！！不过问题来了，太多网站了！！！怎么过滤呢？？？注意正则的开始和结束对应的符,注意follow，不follow就不会继续跟进（也不需要）
        Rule(LinkExtractor(allow=(r'^http://www.hacg.ch/wp/all/anime/.*?/$',)), callback='parse_blue', follow=False),
    )

    def parse_blue(self, response):
        sel = Selector(response)
        title = sel.xpath('//h1[@class="entry-title"]/text()').extract()
        # 要同步回调函数（调用该函数的函数）的item
        item = LlItem()
        # 很关键，没有切片【0】就是列表，切出来就是unicode码
        item['title'] = title[0]
        # 得到自身的网址，重要！！！
        item['url_page'] = response.url
        # sel = Selector(response)
        body = response.body
        pattern = re.compile(r'[熟|生]?([a-z0-9A-Z]{40}|[a-z0-9本站不提供下载A-Z]{54})</')
        blue_link1 = re.findall(pattern, str(body))
        # 利用切片操作得到列表中的字符串或内容，可再次切片对字符串得到想要的
        # 生成器用法！其中切片要注意！
        blue_link0 = (blue_link1[0] if blue_link1 else '')
        blue_link = r'magnet:?xt=urn:btih:' + str(blue_link0)
        item['blue_link'] = blue_link
        yield item

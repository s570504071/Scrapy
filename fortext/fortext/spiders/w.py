#-*-coding:utf-8-*-
from fortext.items import WItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
import re
class WSpider(CrawlSpider):
    name='w'
    allowed_domains=['1kkk.com']
    start_urls=[
        'http://www.1kkk.com/manhua6367/'
    ]
    rules=(
        Rule(LinkExtractor(allow=(r'http://www.1kkk.com/(ch[0-9]{3}-[0-9]{6})/',)),callback='parse_w', follow=True),
    )
    def parse(self,response):
        sel=Selector(response)
        item=WItem()
        html_after=sel.xpath('//li/a/@href').extract()
        title=sel.xpath('//li/a/text()').extract()
        #html_url='http://www.1kkk.com'+html_after
        pattern=re.compile('(/ch[0-9]*-[0-9]*/)')
        for i in html_after:
            s=re.findall(pattern,i)
            if s:
                html_url = 'http://www.1kkk.com' + str(s[0])
                item['html_url']=html_url
                yield item
    def parse_w(self):
        #找不到源码直接显示图片地址！！！
        pass

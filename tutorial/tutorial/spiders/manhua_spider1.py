#coding=utf-8
import scrapy
from tutorial.items import ManhuaItem
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
class ManhuaSpider(CrawlSpider):
    name='manhua1'
    allwoed_domains=['dmzj.com']
    start_urls=[
        'http://manhua.dmzj.com/wangxiangxueshenghui'
        ]
    
    rules=(
        #点号需要转义!!!重要！！！
        Rule(LinkExtractor(allow=(r'http://manhua\.dmzj\.com/wangxiangxueshenghui/[0-9]{5}\.shtml',)),callback='parse_manhua',follow=True),
        )
    
    def parse_manhua(self,response):
        sel=Selector(response)
        item=ManhuaItem()
        item['url']=response.url
        #网页有问题!!!还是网页问题！老实看源码分析吧！！！未解决
        item['pic']=sel.xpath('//img/@src').extract()
        return item
#//*[@id="center_box"]/img

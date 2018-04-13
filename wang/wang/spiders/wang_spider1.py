# ccoding=utf-8
# 该文件夹下不能有与项目同名的文件

"""
方法一有错
Traceback (most recent call last):
  File "d:\python27\lib\site-packages\twisted\internet\defer.py", line 653, in _runCallbacks
    current.result = callback(current.result, *args, **kw)
  File "d:\python27\lib\site-packages\scrapy\spiders\__init__.py", line 90, in parse
    raise NotImplementedError

"""
import scrapy
from wang.items import WangItem

class WangSpider(scrapy.Spider):
    name = 'wang1'
    allowed_domains = ['dmzj.com']
    start_urls = [
        'https://manhua.dmzj.com/wangxiangxueshenghui'
        ]

    def parse(self, response):
        item = WangItem()
        for sel in response.xpath('//div/ul/li/a'):
            item['url'] = sel.xpath('./@href').extract()
            yield item

"""
#coding=utf-8
import scrapy
from wang.items import WangItem
class ManhuaSpider(scrapy.Spider):
    name='wang'
    allwoed_domains=['dmzj.com']
    start_urls=[
        'http://manhua.dmzj.com/wangxiangxueshenghui'
        ]
    def parse(self,response):
        #filename=response.url.split("/")[-2]
        #with open(filename,'wb') as f:
            #f.write(response.body)
        for sel in response.xpath('//div[@class="cartoon_online_border"]//ul//li'):
            item=WangItem()
            slist = []
            title = sel.xpath('.//a/@title').extract()
            for s in title:
            	s.encode('gb2312')
            	slist.append(s)
            item['title']=  slist
            item['url']='http://manhua.dmzj.com'+sel.xpath('.//a/@href').extract()[0]
            yield item

"""

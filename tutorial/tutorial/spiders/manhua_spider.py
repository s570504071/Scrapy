#coding=utf-8
import scrapy
from tutorial.items import ManhuaItem
class ManhuaSpider(scrapy.Spider):
    name='manhua'
    allwoed_domains=['dmzj.com']
    start_urls=[
        'http://manhua.dmzj.com/wangxiangxueshenghui'
        ]
    def parse(self,response):
        #filename=response.url.split("/")[-2]
        #with open(filename,'wb') as f:
            #f.write(response.body)
        for sel in response.xpath('//div[@class="cartoon_online_border"]//ul//li'):
            item=ManhuaItem()
            item['title']=sel.xpath('.//a/@title').extract()
            item['link']='http://manhua.dmzj.com'+sel.xpath('.//a/@href').extract()[0]
            yield item

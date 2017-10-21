#-*-coding:utf-8-*-
import scrapy
from fortext.items import LiuliItem
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule
#from scrapy.contrib.linkextractors import LinkExtractor
import re
#命令行输入：scrapy crawl liuli -o liuli.json
class LiuliSpider(CrawlSpider):
    name='liuli'
    allowed_domains=['hacg.ch']
    start_urls=[
        'http://www.hacg.ch/wp/category/all/anime/'
    ]
    '''
    rules=(
        Rule(LinkExtractor(allow=(r'http://www.hacg.ch/wp/category/all/anime/page/[0-9]*/',)),callback='parse_gethtml', follow=True),
        Rule(LinkExtractor(allow=(r'http://www.hacg.ch/wp/category/all/anime/.*?/',)), callback='parse_blue',follow=True),
    )
    '''
    def parse(self,response):
        #页数，也可写python语句从网站中获取，但这里偷懒直接看网址得到共79页
        num=79
        base_url='http://www.hacg.ch/wp/category/all/anime/page/{0}/'
        for n in range(1,num+1):
            ##最关键的函数！！！
            yield scrapy.Request(base_url.format(n), dont_filter=True, callback=self.parse_html)
    def parse_html(self,response):
        sel=Selector(response)
        item=LiuliItem()
        #另外记最好
        #title=sel.xpath('//h1[@class="entry-title"]/a/text()').extract()
        link=sel.xpath('//h1[@class="entry-title"]/a/@href').extract()
        for i in link:
            #很好
            yield scrapy.Request(i, dont_filter=True, callback=self.parse_blue, meta={'item': item})
    def parse_blue(self,response):
        sel = Selector(response)
        title = sel.xpath('//h1[@class="entry-title"]/text()').extract()
        #要同步回调函数（调用该函数的函数）的item
        item = response.meta['item']
        #很关键，没有切片【0】就是列表，切出来就是unicode码
        item['title'] =title[0]
        #得到自身的网址，重要！！！
        item['url_page']=response.url
        #sel = Selector(response)
        body=response.body
        pattern = re.compile(r'[熟|生]?([a-z0-9A-Z]{40}|[a-z0-9本站不提供下载A-Z]{54})</')
        blue_link1 = re.findall(pattern,str(body))
        # 利用切片操作得到列表中的字符串或内容，可再次切片对字符串得到想要的
        #生成器用法！其中切片要注意！
        blue_link0 = (blue_link1[0] if blue_link1 else '')
        blue_link = r'magnet:?xt=urn:btih:' + str(blue_link0)
        item['blue_link']=blue_link
        '''
        应该有个判断的条件：当字典blue_link不为空时才返回，即：
        if blue_link:
            yield item
        
        
        '''
        yield item

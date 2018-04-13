# -*-coding:utf-8-*-
import scrapy
import os
import urllib
from myhero.items import MyheroItem


class HeroSpider(scrapy.Spider):
    """
    该网站的布置很规律，爬虫简单，注意设置中robot=false...就行了
    还有就是在每一话第一页，不但要爬图片，也要爬下一页的url，懂得yield用法就会用了
    yield与return是不一样的，一旦return，之后的语句就不输出，而yield之后语句会执行直到没有可执行的内容
    """
    name = 'myhero'
    allowed_domains = ['myherocn.com']
    start_urls = ['http://www.myherocn.com/manhua/index{0}.shtml'.format(i) for i in range(1, 5)]

    item = MyheroItem()

    def savepic(self, picsrc):
        if picsrc:
            file_path = os.path.join("D:\\hero", "{0}".format((picsrc[0][-10:]).replace('/', '-')))
        if os.path.exists(file_path):
            pass
        else:
            urllib.urlretrieve(picsrc[0], file_path)

    def parse(self, response):
        for sel in response.xpath('/html/body/div[5]/div[1]/div[3]/ul/li/a/@href').extract():
            yield scrapy.Request(sel, callback=self.page)

    def page(self, response):
        self.item = MyheroItem()
        pic = response.xpath("/html/body/div[2]/div[4]/p/img/@src").extract()
        pic1 = response.xpath("/html/body/div[2]/div[4]/img/@src").extract()
        pre = "http://www.myherocn.com"
        if pic and pre not in pic[0]:
            pic[0] = pre + pic[0]
        if pic1 and pre not in pic1[0]:
            pic1[0] = pre + pic1[0]
        self.item['page_url'] = response.url
        self.item['pic'] = pic or pic1 or ' '
        self.savepic(self.item['pic'])
        yield self.item

        url = response.xpath("/html/body/div[2]/div[7]/ul/li[3]/a/@href").extract()
        fullurl = "http://www.myherocn.com/manhua/" + url[0]
        if url != '#':
            yield scrapy.Request(fullurl, callback=self.page)


"""
/html/body/div[2]/div[7]/ul/li[3]/a
/html/body/div[2]/div[7]/ul/li[3]/a
/html/body/div[2]/div[7]/ul/li[3]/a


/html/body/div[2]/div[7]/ul/li[3]/a


/html/body/div[2]/div[4]/img
/html/body/div[2]/div[4]/img
/html/body/div[2]/div[4]/img

/html/body/div[2]/div[4]/center/img
"""
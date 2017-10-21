# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ManhuaItem(scrapy.Item):
    url=scrapy.Field()
    pic=scrapy.Field()
    title=scrapy.Field()
    link=scrapy.Field()
 
 
class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  #电影名称
    description = scrapy.Field()  #电影描述
    url = scrapy.Field()  #抓取的url

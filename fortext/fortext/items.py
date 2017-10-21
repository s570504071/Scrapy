# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FortextItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class TestItem(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    description=scrapy.Field()
class WItem(scrapy.Item):
    pic_url=scrapy.Field()
    html_url=scrapy.Field()
    title=scrapy.Field()
class LiuliItem(scrapy.Item):
    blue_link=scrapy.Field()
    url_page=scrapy.Field()
    title=scrapy.Field()
class LlItem(scrapy.Item):
    blue_link=scrapy.Field()
    url_page=scrapy.Field()
    title=scrapy.Field()
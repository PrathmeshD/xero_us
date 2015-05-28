# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class XeroUsItem(scrapy.Item):
    firstName = scrapy.Field()
    lastName = scrapy.Field()
    phoneNumber = scrapy.Field()
    email = scrapy.Field()
    companyName = scrapy.Field()
    lvl = scrapy.Field()
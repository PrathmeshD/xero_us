# -*- coding: utf-8 -*-
import scrapy
import json
import requests
import string

from xero_us.items import XeroUsItem
from scrapy.contrib.spiders import CrawlSpider, Rule

class XeroUsAccSpider(scrapy.Spider):
    name = "xero_us"
    allowed_domains = ["www.xero.com"]
    start_urls = [
        'https://api.import.io/store/data/9bcfa7ff-88cb-4266-a8b5-c253e8cfaa23/_query?input/webpage/url=https%3A%2F%2Fwww.xero.com%2Fus%2Fadvisors%2F%3Fcountry%3Dus%26service%3Daccountant%26view%3Dmap&_user=dfc92ca6-a5e4-43bf-bd7e-ecfd6bebeb0e&_apikey=dfc92ca6-a5e4-43bf-bd7e-ecfd6bebeb0e%3AzQomHBBGgjXSHQocUFw0SYTwK65nDwgiRMjhw1UXjv%2BfLL%2B3MjKyXIl2uO1XA9AAlDEGZ%2FWsV9jiIHTrSX1cvw%3D%3D',
        #'https://api.import.io/store/data/9c188f76-289c-408b-a8b3-9c80697d4aa6/_query?input/webpage/url=https%3A%2F%2Fwww.xero.com%2Fus%2Fadvisors%2F%3Fcountry%3Dus%26service%3Daccountant%26view%3Dmap&_user=dfc92ca6-a5e4-43bf-bd7e-ecfd6bebeb0e&_apikey=dfc92ca6-a5e4-43bf-bd7e-ecfd6bebeb0e%3AzQomHBBGgjXSHQocUFw0SYTwK65nDwgiRMjhw1UXjv%2BfLL%2B3MjKyXIl2uO1XA9AAlDEGZ%2FWsV9jiIHTrSX1cvw%3D%3D'
    ]

    def parse(self, response):
        #load JSON key,value information into jsonresponse
        jsonresponse = json.loads(response.body_as_unicode())

        for contacts in jsonresponse['results']:
            item = XeroUsItem()

            temp = 1

            nameset = contacts['value'].split()
            item['firstName'] = string.capwords(nameset[1])
            try:
                item['lastName'] = string.capwords(nameset[2])
            except IndexError:
                temp = 0
                item['lastName'] = ""

            try:
                item['lastName'] += " " + string.capwords(nameset[3])
            except KeyError:
                pass
            except IndexError:
                pass

            item['firstName'] = item['firstName'].replace(',', '')
            try:
                item['lastName'] = item['lastName'].replace(',', '')
                item['lastName'] = item['lastName'].replace(' Cpa', '')
                item['lastName'] = item['lastName'].replace(' Managing', '')
            except KeyError:
                pass
            except AttributeError:
                pass

            item['email'] = contacts['email_link'][7:]
            item['phoneNumber'] = contacts['email_value']
            item['companyName'] = string.capwords(contacts['name_value'])

            item['lvl'] = contacts['status_value']

            yield item
# -*- coding: utf-8 -*-

# Scrapy settings for xero_us project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'xero_us'

SPIDER_MODULES = ['xero_us.spiders']
NEWSPIDER_MODULE = 'xero_us.spiders'

ITEM_PIPELINES = {
    'xero_us.pipelines.XeroUsPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xero_us (+http://www.yourdomain.com)'

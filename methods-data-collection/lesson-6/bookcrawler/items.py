# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookcrawlerItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    source = scrapy.Field()
    authors = scrapy.Field()
    price = scrapy.Field()
    sale_price = scrapy.Field()
    rate = scrapy.Field()

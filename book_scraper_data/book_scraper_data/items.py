# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookScraperDataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    price = scrapy.Field()
    in_stock_qty = scrapy.Field()
    ratings = scrapy.Field()
    description = scrapy.Field()
    product_url = scrapy.Field()
    upc = scrapy.Field()


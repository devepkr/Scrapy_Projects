# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy

class BookScraperItem(scrapy.Item):
    book_breadcrumbs = scrapy.Field()
    book_name = scrapy.Field()
    book_price = scrapy.Field()
    book_rating = scrapy.Field()
    book_description = scrapy.Field()
    book_url = scrapy.Field()
    book_attributes = scrapy.Field()

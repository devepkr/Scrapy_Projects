import scrapy
import re
from book_scraper_data.items import BookScraperDataItem

class BooksSpiderSpider(scrapy.Spider):
    name = "books_spider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        product_links = response.css('article.product_pod h3 a::attr(href)').getall()
        for link in product_links:
            yield response.follow(link, callback=self.extract_prodcute_page)
        
        # pagination
        next_page_button = response.css('li.next a::attr(href)').get()
        if next_page_button:
            yield response.follow(next_page_button, callback=self.parse)
        
    def extract_prodcute_page(self,response):
        item = BookScraperDataItem()
        item['title'] = response.css('article[class="product_page"] h1::text').get()
        item['image_url'] = response.css('#product_gallery img::attr(src)').get()
        item['price'] = response.css('article[class="product_page"] .price_color::text').get()
        
        # stock_text = response.css('p.instock.availability::text').getall()
        stock_text = [text.strip().split()[0] for text in response.xpath("//p[@class='instock availability']/text()").getall() if text.strip()]
        # match = re.search(r'\d+', ' '.join(stock_text))
        item['in_stock_qty'] = stock_text


        
        item['ratings'] = response.css('.star-rating::attr(class)').get()
        item['description'] = response.css('#product_description ~ p::text').get()
        
        item['product_url'] = response.url

        # Extract UPC and other product info
        table_rows = response.css('table.table.table-striped tr')
        for row in table_rows:
            header = row.css('th::text').get()
            value = row.css('td::text').get()
            if header == 'UPC':
                item['upc'] = value
        yield item


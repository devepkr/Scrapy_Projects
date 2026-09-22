import scrapy
from bookscraper_1.items import BookScraperItem

class BookesScraperSpider(scrapy.Spider):
    name = "bookes_scraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # click on product page one by one and get the data for each product
        product_links = response.css("article.product_pod h3 a::attr(href)").getall()
        for link in product_links:
            yield response.follow(link, callback=self.extract_product_data)
            
        # Follow pagination links
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def extract_product_data(self, response):
        item = BookScraperItem()
        item['book_breadcrumbs'] = response.css("ul.breadcrumb li a::text").getall()
        item['book_name'] = response.css("article[class='product_page'] h1::text").get()
        item['book_price'] = response.css(".price_color::text").get()
        item['book_rating'] = response.css(".star-rating::attr(class)").get()
        item['book_description'] = response.css("#product_description ~ p::text").get()
        item['book_url'] = response.url
        attributes = {}
        for row in response.css('table.table-striped tr'):
            key = row.css('th::text').get()
            value = row.css('td::text').get()
            if key and value:
                attributes[key.strip()] = value.strip()
        item['book_attributes'] = attributes
        yield item

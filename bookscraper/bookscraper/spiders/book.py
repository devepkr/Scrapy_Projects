import scrapy
from bookscraper.items import BookscraperItem
page_count = 1

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    page_count = 1
    def parse(self, response):
        card_section = response.css("article.product_pod")
        for card in card_section:
            item = BookscraperItem()
            item["title"] = card.css(".product_pod h3 a::text").get()
            item["price"] = card.css(".product_pod .price_color::text").get()
            item["rating"] = card.css(".star-rating::attr(class)").get()
            item['url'] = card.css(".product_pod h3 a::attr(href)").get()
            yield item
        yield from self.pagination(response)

    def pagination(self, response):
        if self.page_count < 5:
            next_page = response.css(".pager li.next a::attr(href)").get()
            if next_page:
                self.page_count += 1
                yield response.follow(next_page, self.parse)

    
    """
    def make_request(self, request):
        card_section = request.css("article.product_pod")
        for card in card_section:
            title = card.css(".product_pod h3::text").get()
            price = card.css(".product_pod .price_color::text").get()
            rating = card.css(".star-rating::attr(class)").get()
            yield {
                "title": title,
                "price": price,
                "rating": rating,
            }
            next_page = request.css(".pager li.next a::attr(href)").get()
            if next_page:
                yield request.follow(next_page, self.make_request)"""



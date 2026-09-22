import scrapy
from quotes_projects.items import QuotesProjectsItem


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        listed_page = "div.quote"
        for quotes_item in response.css(listed_page):

            item = QuotesProjectsItem(
                title=quotes_item.css("[itemprop='text']::text").get(),
                author=quotes_item.css("[itemprop='author']::text").get(),
                tags=quotes_item.css("[class='tag']::text").getall(),
            )
            yield item

        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
            
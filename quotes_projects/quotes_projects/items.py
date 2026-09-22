# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass, field



@dataclass
class QuotesProjectsItem:
    title: str = ""
    author: str = ""
    tags: list[str] = field(default_factory=list)




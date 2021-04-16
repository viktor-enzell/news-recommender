import scrapy

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    text = scrapy.Field()

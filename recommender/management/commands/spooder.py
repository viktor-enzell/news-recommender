import scrapy
from item import NewsItem

class Spider(scrapy.Spider):
    name = 'spooder'
    start_urls = ['https://omni.se/professor-gor-som-uppsala-det-ger-fin-boosteffekt/a/56Kxw6']

    def parse(self, response):
        item = NewsItem()
        
        for article in response.css('.article-resourcecolumn--large'):
            yield {
                'title': article.xpath('h1/text()').get(),
                'text': article.css('.resource--text').get()
            }

        next_page = response.css('.article-link a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

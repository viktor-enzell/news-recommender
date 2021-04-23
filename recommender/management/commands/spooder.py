import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class Spider(CrawlSpider):
    name = 'news_crawler'
    allowed_domains = [
        'www.bbc.com',
    ]
    start_urls = [
        'https://www.bbc.com/news'
    ]

    rules = (
        Rule(
            LinkExtractor(allow=('news/', )),
            callback='parse_news',
            follow=True
        ),
    )

    def parse_news(self, response):
        for article in response.xpath('//article'):
            text = []
            for p in article.xpath('//p/text()'):
                text.append(p.get())
            yield {
                'url': response.url,
                'title': article.xpath('//h1/text()').get(),
                'text': ' '.join(text),
            }
            break

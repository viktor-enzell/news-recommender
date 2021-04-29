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
        article = response.xpath('//article[contains(@class, "ArticleWrapper")]').extract_first(default='not_found')
        if article != 'not_found':
            bold = response.xpath('//article//p/b/text()').get();
            text = [bold]
            for p in response.xpath('//article//p/text()'):
                t = p.get()
                text.append(t)
            yield {
                'url': response.url,
                'title': response.xpath('//article//h1/text()').get(),
                'text': ' '.join(text),
            }

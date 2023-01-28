import scrapy
import random


class QuotesSpider(scrapy.Spider):
    name = "blogs"
    start_urls = [
        'https://blog.pengfeima.cn',
    ]

    def parse(self, response):
        filename = self.name + str(random.random())[-5:] +'.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        for a in response.css('a::attr(href)').getall():
            if 'http' in a :
                continue
            yield response.follow(url=a, callback=self.parse)

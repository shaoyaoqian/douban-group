import scrapy
import random

from urllib.parse import urlparse


class ImageItem(scrapy.Item):
    # ... other item fields ...
    image_urls = scrapy.Field()
    images = scrapy.Field()
    domain = scrapy.Field()
    album = scrapy.Field()

class QuotesSpider(scrapy.Spider):
    name = "blogs"
    start_urls = [
        'https://dusays.com',
        # 'https://blog.pengfeima.cn',
        # 'https://blog.shishuai.monster',
        # 'https://skyreeves.cn/'
    ]
    
    custom_settings = {
        'JOBDIR': 'jobs/blogs',
    }

    def parse(self, response):
        for a in response.css('img::attr(src)').getall():
            item = ImageItem()
            item['image_urls'] = [a]
            item['domain'] = urlparse(response.url).netloc
            yield item
        
        foramts = ['jpg','jpeg','webp','gif','svg','png']

        for a in response.css('a::attr(href)').getall():
            for f in foramts:
                if f in a:
                    item = ImageItem()
                    item['image_urls'] = [a]
                    item['domain'] = urlparse(response.url).netloc
                    yield item
            if 'http' in a :
                continue
            else:
                yield scrapy.Request(url=response.urljoin(a), callback=self.parse)

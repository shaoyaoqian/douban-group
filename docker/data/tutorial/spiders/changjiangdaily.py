import scrapy
import random
from pathlib import Path
from urllib.parse import urlparse

class QuotesSpider(scrapy.Spider):
    name = "changjiangdaily"
    start_urls = [
        'http://cjrb.cjn.cn/html/2023-02/11/node_1.htm',
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-1]
        content = response.css('#scroller').get()
        filename = f'hubei_daily.html'
        if content is not None:
            with open(filename,'a') as f:
                f.write(content)
        
        for a in response.css('li'):
            local_url = a.css('a::attr(href)').get()
            print(local_url)
            if local_url is not None and '..' in local_url:
                yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse)

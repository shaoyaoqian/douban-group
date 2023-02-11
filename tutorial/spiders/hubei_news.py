import scrapy

import time

year_month = time.strftime("%Y%m",time.localtime())
date = time.strftime("%d",time.localtime())
class QuotesSpider(scrapy.Spider):
    name = "hubei_news"
    start_urls = [
        f'https://epaper.hubeidaily.net/pad/column/{year_month}/{date}/node_01.html',
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-1]
        content = response.css('#scroller').get()
        filename = f'content.html'
        if content is not None:
            with open(filename,'a') as f:
                f.write(content)
        
        for a in response.css('li'):
            local_url = a.css('a::attr(href)').get()
            print(local_url)
            if local_url is not None and '..' in local_url:
                yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse)

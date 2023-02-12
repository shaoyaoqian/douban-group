import scrapy
from urllib.parse import urlparse
import time

year_month = time.strftime("%Y-%m",time.localtime())
date = int(time.strftime("%d",time.localtime()))
class QuotesSpider(scrapy.Spider):
    name = "changjiang_daily"
    start_urls = [
        f'http://cjrb.cjn.cn/html/{year_month}/{date}/node_1.htm',
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-1]

        for a in response.css('#pageLink'):
            local_url = a.css('a::attr(href)').get()
            print(local_url)
            yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse)
        
        for a in response.css('.one'):
            local_url = a.css('a::attr(href)').get()
            print(local_url)
            yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse_content)
    
    def parse_content(self, response):
        h1 = response.css('.text_c h1').get()
        h2 = response.css('.text_c h2').get()
        content = response.css('#ozoom').get()
        filename = f'changjiang_daily.html'
        if content is not None:
            with open(filename,'a') as f:
                if h1 is not None:
                    f.write(h1)
                if h2 is not None:
                    f.write(h2)
                f.write(content)

import scrapy
import time


from .sort_news import find_key_words

year_month = time.strftime("%Y%m",time.localtime())
date = int(time.strftime("%d",time.localtime()))
class QuotesSpider(scrapy.Spider):
    name = "hubei_daily"
    start_urls = [
        f'https://epaper.hubeidaily.net/pad/column/{year_month}/{date}/node_01.html',
        f'https://epaper.hubeidaily.net/pad/column/{year_month}/{date}/node_02.html',
        f'https://epaper.hubeidaily.net/pad/column/{year_month}/{date}/node_03.html',
        f'https://epaper.hubeidaily.net/pad/column/{year_month}/{date}/node_04.html',
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-1]

        for a in response.css('li'):
            local_url = a.css('a::attr(href)').get()
            print(local_url)
            if local_url is not None and 'content' in local_url:
                yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse_content)
    
    def parse_content(self, response):
        content = response.css('#scroller').get()
        filename = f'hubei_daily.html'
        filename_2 = f'hubei_daily_sorted.html'
        if content is not None:
            with open(filename,'a') as f:
                f.write(content)
            if find_key_words(content):
                with open(filename_2,'a') as f:
                    f.write(content)

        


        

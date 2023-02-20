import scrapy
import time


from .sort_news import find_key_words

article_header_raw = '<h1>{main_title}</h1><h2>{sub_title}</h2><h3>发布时间：{date}&ensp;&ensp;原文链接：<a href="{url}">{kind}</a></h3>'
now_in_beijing = time.localtime(time.time()+28800)

year_month = time.strftime("%Y%m",now_in_beijing)
date = int(time.strftime("%d",now_in_beijing))
class QuotesSpider(scrapy.Spider):
    name = "hubei_daily"
    start_urls = [
        f'https://epaper.hubeidaily.net/pad/column/{year_month}/{date}/node_01.html',
    ]
    
    def parse(self, response):
        page = response.url.split("/")[-1]

        for a in response.css('li'):
            local_url = a.css('a::attr(href)').get()
            # print(local_url)
            if local_url is not None and 'content' in local_url:
                yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse_content)

    def parse_content(self, response):
        main_title = response.css('#scroller #main-title').get()
        sub_title = response.css('#scroller #sub-title').get()
        date = response.css('#scroller #author').get()
        url = response.url
        content = response.css('#scroller #content').get()

        article_header = article_header_raw.format(main_title=main_title,sub_title=sub_title,date=date,url=url,kind='湖北日报')
        
        filename = f'hubei_daily.html'
        filename_2 = f'hubei_daily_sorted.html'
        if content is not None:
            with open(filename,'a') as f:
                f.write(article_header)
                f.write(content)
            keywords = find_key_words(content)
            if len(keywords) > 0:
                with open(filename_2,'a') as f:
                    f.write(article_header)
                    f.write('<h3>关键词：' + ', '.join(keywords)+'</h3>')
                    f.write(content)
        


        

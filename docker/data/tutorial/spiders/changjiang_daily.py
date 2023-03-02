import scrapy
from urllib.parse import urlparse
import time

from .sort_news import find_key_words

article_header_raw = '<h1>{main_title}</h1><h2>{sub_title}</h2><h3>发布时间：{date}&ensp;&ensp;原文链接：<a href="{url}">{kind}</a></h3>'

now_in_beijing = time.localtime(time.time()+28800)
year_month = time.strftime("%Y-%m",now_in_beijing)
date = time.strftime("%d",now_in_beijing)
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
        
        for a in response.css('#titleList li'):
            local_url = a.css('a::attr(href)').get()
            print(local_url)
            yield scrapy.Request(url=response.urljoin(local_url), callback=self.parse_content)
    
    def parse_content(self, response):
        main_title = response.css('.text_c h1::text').get()
        sub_title = response.css('.text_c h2::text').get() or ''
        date = time.strftime("%Y年%m月%d日",now_in_beijing)
        url = response.url
        content = response.css('#ozoom').get()
        article_header = article_header_raw.format(main_title=main_title,sub_title=sub_title,date=date,url=url,kind='长江日报')
        filename = f'changjiang_daily.html'
        filename_2 = f'changjiang_daily_sorted.html'
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
            

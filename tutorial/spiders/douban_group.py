import scrapy
import random


class QuotesSpider(scrapy.Spider):
    name = "douban-group"

    def start_requests(self):
        urls = [
            'https://www.douban.com/group/729203/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = self.name + str(random.random())[-5:] +'.html'
        for tr in response.css('tr'):
            tds = tr.css('td')
            data = [tds[0].css('td a::attr(title)').get(),
                tds[0].css('td a::attr(href)').get(),
                tds[1].css('td a::text').get(),
                tds[1].css('td a::attr(href)').get(),
                tds[3].css('td::text').get()]
            if '最后回应' not in data:
                yield response.follow(url=data[1], callback=self.parse_item)

    def parse_item(self, response):
        item = dict()
        item['filename'] = '博文' + str(random.random())[-5:] +'.html'
        item['url'] = response.url
        item['title'] = response.css('.article h1').get()
        item['content'] = response.css('#link-report .topic-content').get()
        comments = []
        for comment_item in response.css('.comment-item'):
            comments.append(comment_item.css('.reply-doc').get())
        item['comments'] = comments
        with open(item['filename'], 'wb') as f:
            f.write(response.body)
        yield item
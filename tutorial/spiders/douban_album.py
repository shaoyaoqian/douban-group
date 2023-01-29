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
    name = "douban-album"
    ''''
    遍历相册的思路：先进入一个相册，打开单张相片，相片右侧会展示作者其他热门相册，但是这样并不能爬取作者所有相册。
    用法：需要知道相册名和相册中一张相片的地址才能启动爬虫。
    '''
    def start_requests(self):
        urls = [
            # 'https://www.douban.com/photos/photo/2669839083/',
            # 'https://www.douban.com/photos/photo/2286018094/',
            # 'https://www.douban.com/photos/photo/1900158105/',
            # 'https://www.douban.com/photos/photo/2345626212/',
            'https://www.douban.com/photos/photo/2716006781/',
        ]
        names = [
            # '树影婆娑',
            # '皖南秋迟',
            # '惊蛰 杭州',
            # '傻冒叔的相册-雁荡，等一场烟雨',
            'H&M 家居参考',
        ]
        for url,name in zip(urls,names):
            yield scrapy.Request(url=url, callback=self.parse_single_picture, meta={'album': name})



    def parse_album(self, response):
        # 找到相册中的第一张图片
        a = response.css('.photolst').css('.photo_wrap a::attr(href)').get()
        url = a
        yield response.follow(url=url, callback=self.parse_single_picture, meta=response.meta)



    def parse_single_picture(self, response):
        # 保存图片
        a = response.css('.image-show-inner').css('img::attr(src)').get()
        item = ImageItem()
        item['image_urls'] = [a]
        item['domain'] = urlparse(response.url).netloc
        print(response.meta)
        item['album'] = response.meta['album']
        yield item
        # 下一张图片的链接
        a = response.css('#next_photo::attr(href)').get()
        if a :
            yield response.follow(url=a, callback=self.parse_single_picture, meta=response.meta)
        # 找到其他相册
        urls = response.css('.album-list').css('.info a::attr(href)').getall()
        names = response.css('.album-list').css('.info a::text').getall()
        for url,name in zip(urls,names):
            yield response.follow(url=url, callback=self.parse_album, meta={'album': name})



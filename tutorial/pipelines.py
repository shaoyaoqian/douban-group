# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import redis
import os
PATH = 'output'
REDIS_PORT = 29384
DATABASE = 2



# url
# title
# time
# content
# comments
redis_douban_group_all_topics     = 'douban:group:all:topics'
redis_douban_group_topic_author      = 'douban:group:topicid:{topicid:s}:author:name'
redis_douban_group_topic_author_link      = 'douban:group:topicid:{topicid:s}:author:link'
redis_douban_group_topic_created_time      = 'douban:group:topicid:{topicid:s}:created:time'
redis_douban_group_topic_created_ip     = 'douban:group:topicid:{topicid:s}:created:ip'
redis_douban_group_topic_url      = 'douban:group:topicid:{topicid:s}:url'
redis_douban_group_topic_title    = 'douban:group:topicid:{topicid:s}:title'
redis_douban_group_topic_time     = 'douban:group:topicid:{topicid:s}:time'
redis_douban_group_topic_content  = 'douban:group:topicid:{topicid:s}:content'
redis_douban_group_topic_comments = 'douban:group:topicid:{topicid:s}:comments'

class RedisWriterPipeline(object):
    """
    写入redis数据库的pipline
    """

    def __init__(self):
        self.file = None
        if not os.path.exists(PATH):
            os.mkdir(PATH)

    def process_item(self, item, spider):
        """
        处理item
        """
        r = redis.StrictRedis(host='localhost', port=REDIS_PORT, db=DATABASE)
        topic_url = item['url']
        topic_id = topic_url.split('/')[-2]
        topic_title = item['title']
        topic_content = item['content']
        topic_comments = item['comments']
        topic_author = item['author']
        topic_author_link = item['author_link']
        topic_created_time = item['create-time']
        topic_created_ip = item['create-ip']
        r.set(redis_douban_group_topic_author.format(topicid=topic_id), topic_author)
        r.set(redis_douban_group_topic_author_link.format(topicid=topic_id), topic_author_link)
        r.set(redis_douban_group_topic_created_time.format(topicid=topic_id), topic_created_time)
        r.set(redis_douban_group_topic_created_ip.format(topicid=topic_id), topic_created_ip)
        r.sadd(redis_douban_group_all_topics, topic_id)
        r.set(redis_douban_group_topic_url.format(topicid=topic_id), topic_url)
        old_topic_content = r.get(redis_douban_group_topic_content.format(topicid=topic_id))
        # 原本没有内容时，添加内容
        if old_topic_content == None:
            r.set(redis_douban_group_topic_content.format(topicid=topic_id), topic_content)
        # HACK: 当新内容长度大于旧内容时才更新
        elif len(topic_content) > len(old_topic_content):
            r.set(redis_douban_group_topic_content.format(topicid=topic_id), topic_content)
        r.set(redis_douban_group_topic_title.format(topicid=topic_id), topic_title)
        # HACK: 如果评论内容修改了，会新增加一条
        for topic_comment in topic_comments:
            r.sadd(redis_douban_group_topic_comments.format(topicid=topic_id), topic_comment)
        r.save()
        return item


from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class ImagePipeline(ImagesPipeline):

    #自定义文件路径和文件名
    def file_path(self, request, response=None, info=None):
        domain = request.meta['item']['domain']
        album = request.meta['item']['album'] or 'default'
        image_guid = request.url.split('/')[-1]
        print(image_guid)
        print(domain)
        return 'full/%s/%s/%s' % (domain, album, image_guid)

    #用get_media_requests方法进行下载控制，返回一个requests对象
    #对象被Pipeline处理，下载结束后，默认直接将结果传给item_completed方法
    def get_media_requests(self, item, info):
        for url in item['image_urls']:
            yield scrapy.Request(url, meta={'item': item})


    def item_completed(self,results,item,info):
        #创建图片存储路径
        path=[x['status'] for ok,x in results if ok]
        print(path)
        #判断图片是否下载成功，若不成功则抛出DropItem提示
        if not path:
            raise DropItem('Item contains no images')
        print(u'正在保存图片：', item['image_urls'])
        return item


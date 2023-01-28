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
        r.sadd(redis_douban_group_all_topics, topic_id)
        r.set(redis_douban_group_topic_url.format(topicid=topic_id), topic_url)
        old_topic_content = r.get(redis_douban_group_topic_content.format(topicid=topic_id))
        # HACK: 当新内容长度大于旧内容时才更新
        if old_topic_content != None and len(topic_content) > len(old_topic_content):
            r.set(redis_douban_group_topic_content.format(topicid=topic_id), topic_content)
        r.set(redis_douban_group_topic_title.format(topicid=topic_id), topic_title)
        # HACK: 如果评论内容修改了，会新增加一条
        for topic_comment in topic_comments:
            r.sadd(redis_douban_group_topic_comments.format(topicid=topic_id), topic_comment)
        r.save()
        return item


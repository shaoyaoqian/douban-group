
# extract data and write it into a json file

import json
import redis
import os
PATH = 'output'
REDIS_PORT = 29384
DATABASE = 2
JSONFILE = 'data.json'



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


redis_douban_group_topic_author      = 'douban:group:topicid:{topicid:s}:author:name'
redis_douban_group_topic_author_link      = 'douban:group:topicid:{topicid:s}:author:link'
redis_douban_group_topic_created_time      = 'douban:group:topicid:{topicid:s}:created:time'
redis_douban_group_topic_created_ip     = 'douban:group:topicid:{topicid:s}:created:ip'


r = redis.StrictRedis(host='localhost', port=REDIS_PORT, db=DATABASE)

data = []

for i in r.smembers(redis_douban_group_all_topics):
    topic_id = i.decode('utf-8')
    topic_content = r.get(redis_douban_group_topic_content.format(topicid=topic_id))
    topic_title = r.get(redis_douban_group_topic_title.format(topicid=topic_id))
    topic_url = r.get(redis_douban_group_topic_url.format(topicid=topic_id))
    topic_author = r.get(redis_douban_group_topic_author.format(topicid=topic_id))
    topic_author_link = r.get(redis_douban_group_topic_author_link.format(topicid=topic_id))
    topic_created_ip = r.get(redis_douban_group_topic_created_ip.format(topicid=topic_id))
    topic_created_time = r.get(redis_douban_group_topic_created_time.format(topicid=topic_id))
    print(topic_title,topic_id,topic_url,topic_content)
    topic_comments = []
    for comment in r.smembers(redis_douban_group_topic_comments.format(topicid=topic_id)):
        topic_comments.append((comment or b'').decode('utf-8'))
    topic = {}
    topic['id'] = topic_id
    topic['content'] = (topic_content or b'').decode('utf-8')
    topic['title']= (topic_title or b'').decode('utf-8')
    topic['url'] =  (topic_url or b'').decode('utf-8')
    topic['comments'] = topic_comments
    topic['author'] = (topic_author or b'').decode('utf-8')
    topic['author_link'] = (topic_author_link or b'').decode('utf-8')
    topic['create-time'] = (topic_created_time or b'').decode('utf-8')
    topic['create-ip'] = (topic_created_ip or b'').decode('utf-8')
    data.append(topic)

with open(JSONFILE, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

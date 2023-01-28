
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



r = redis.StrictRedis(host='localhost', port=REDIS_PORT, db=DATABASE)

data = []

for i in r.smembers(redis_douban_group_all_topics):
    topic_id = i.decode('utf-8')
    topic_content = r.get(redis_douban_group_topic_content.format(topicid=topic_id))
    topic_title = r.get(redis_douban_group_topic_title.format(topicid=topic_id))
    topic_url = r.get(redis_douban_group_topic_url.format(topicid=topic_id))
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
    data.append(topic)

with open(JSONFILE, 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

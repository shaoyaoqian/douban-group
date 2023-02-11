# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15',
    'Cookie': '__utma=30149280.131450382.1674023924.1674892442.1674963921.11; __utmb=30149280.50.10.1674963921; __utmc=30149280; __utmt=1; __utmv=30149280.6250; __utmz=30149280.1674023924.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_doumail_num=0; push_noty_num=0; ap_v=0,6.0; frodotk_db="39aa2148ce7b3642acfe63da6b71a2c6"; ck=bIaF; dbcl2="62503351:S+2R5Qca+zI"; __gpi=UID=00000ba0fa05b967:T=1673280250:RT=1674879201:S=ALNI_MYsKrZQ3V2f0iwU0Z-8cyye8ruUEQ; gr_user_id=797e93ce-6d9a-4eb6-b446-323350cc5cbe; viewed="10559282_30429946"; ct=y; douban-fav-remind=1; __gads=ID=53960aca160e9202-223af47137d900e3:T=1673280250:RT=1673280250:S=ALNI_MbWkZ6Tr33eF2dK8CNbywMkL4JhKw; bid=tkbJxuM15hY; ll="118178"'
}



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'tutorial.pipelines.ImagePipeline': 1,
    # 'tutorial.pipelines.RedisWriterPipeline': 300,
}


#IMAGES_STORE用于设置图片存储路径
IMAGES_STORE='img'

# #IMAGES_THUMBS用于生成大小不同的缩略图
# #以字典形式表示，键为文件名，值为图片尺寸
# IMAGES_THUMBS={
#     'small': (50, 50),
#     'big': (200, 200),}

#以下两个设置可以过滤尺寸小于100的图片
IMAGES_MIN_HEIGHT=10
IMAGES_MIN_WIDTH=10

#IMAGES_EXPIRES用于设置失效期限
#这里是90天，避免管道重复下载最近已经下载过的
IMAGES_EXPIRES=90


# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

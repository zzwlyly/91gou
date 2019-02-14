# -*- coding: utf-8 -*-

# Scrapy settings for shop project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'shop'
BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
SPIDER_MODULES = ['shop.spiders']
NEWSPIDER_MODULE = 'shop.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'shop (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'shop.middlewares.ShopSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    'shop.middlewares.ShopDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
    'shop.middlewares.RotateUserAgentMiddleware': 400,
    'shop.middlewares.MyIPCroxyMiddleware': 450,
    'shop.middlewares.SeleniumJDMiddleware': 550,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
    'shop.pipelines.ShopPipeline': 300,
    # 同步mysql数据库存储管道
    # 'shop.mysqlpipelines.MysqlPipelines': 400,
    # 异步mysql数据库存储管道
    'shop.async_mysqlpipelines.AsyncMysqlPipelines': 500,
    # 存储数据到mongodb
    # 'shop.mongodbpipelines.MongoDBPipelines': 550,
    # 图片存储管道
    'shop.imagepipelines.MyImagesPipeline': 600,
}
# 图片存储的绝对路径
IMAGES_STORE = os.path.join(BASE_DIR, "images")
print(IMAGES_STORE)
# 图片存储大图 缩略图
# IMAGES_THUMBS = {
#     "small": (30, 30),
#     "big": (500, 500),
# }
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html

AUTOTHROTTLE_ENABLED = True

# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

###################  MYSQL 配置 start ############################
DB_SET_MAP = {
    'user': 'root',
    'password': 'zzw12345',
    'host': '127.0.0.1',
    'port': 3306,
    'database': '91gou'
}
################    MYSQL 配置 end  #########################


###############   log settings begin   ######################

LOG_LEVEL = "INFO"

from datetime import datetime
import os

today = datetime.now()

LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)

###############   log settings end   ######################


###################### IP POOL  ############################

ua_path = os.path.join(BASE_DIR, "ip_pool/ua_list.txt")
print(ua_path)
USER_AGENT_LIST = []
with open(ua_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        USER_AGENT_LIST.append(line.strip())

ip_path = os.path.join(BASE_DIR, "ip_pool/proxy_list.txt")
IP_POOL = []
with open(ip_path, "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        IP_POOL.append(line.strip())
###################### IP POOL  ############################

##################### 分布式配置 start ##########################

# # 调度器策略 --- scrapy_redis.scheduler.Scheduler
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#
# # 去重策略 --- scrapy_redis.dupefilter.RFPDupeFilter （此去重器继承scrapy自带的去重器）
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#
# # REDIS配置地址
# REDIS_URL = "redis://127.0.0.1:6379"
#
# # 此开关表示，如果当前分布式爬取关闭后，是否保留原来调度器中去重记录，关系到是否重爬
# SCHEDULER_PERSIST = True

##################### 分布式配置 end ##########################

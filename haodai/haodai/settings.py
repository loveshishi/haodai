# -*- coding: utf-8 -*-

# Scrapy settings for haodai project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'haodai'

SPIDER_MODULES = ['haodai.spiders']
NEWSPIDER_MODULE = 'haodai.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

HTTPPROXY_ENABLED=True

PROXIES=["http://123.206.133.179:1704",
         'http://39.106.202.68:1704',
          'http://120.79.56.156:1704',
          'http://39.106.57.53:1704',
          'http://47.93.203.231:1704',
          'http://140.143.141.236:1704',
          'http://120.78.162.253:1704',
          'http://39.107.96.88:1704',
          'http://39.107.98.78:1704',
          'http://203.195.230.40:1704',
          'http://47.106.117.214:1704',
          'http://39.105.102.177:1704',
          'http://140.143.155.139:1704',
          'http://39.108.3.52:1704',
          'http://47.95.13.99:1704',
          'http://39.104.112.68:1704',
          'http://112.74.172.140:1704',
          'http://112.74.57.120:1704',
          'http://39.108.139.176:1704',
          'http://203.195.204.174:1704',
          'http://47.95.195.216:1704',
          'http://139.199.68.216:1704',
          'http://39.106.57.137:1704',
          'http://39.105.80.9:1704',
          'http://59.110.219.8:1704',
          'http://211.159.147.237:1704',
          'http://39.108.8.146:1704']

DOWNLOAD_TIMEOUT = 5
# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 4

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'haodai.middlewares.HaodaiSpiderMiddleware': 543,
#}

# Enable or disable downloader middle
# wares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'haodai.middlewares.RandomProxyMiddleware': 749,
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'haodai.pipelines.HaodaiPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

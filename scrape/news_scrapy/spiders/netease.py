# -*- coding: utf-8 -*-
from datetime import datetime

import scrapy
import re
from news_scrapy import settings
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


from main.models import Post


class NeteaseSpider(CrawlSpider):
    name = 'netease'
    allowed_domains = ['163.com']
    start_urls = ['http://news.163.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*\.163\.com/\d{2}/\d{4}/\d{2}/.*\.html'), callback='parse_post', follow=True),
    )

    def parse_post(self, response):
        content = '<br>'.join(response.css('.post_text p::text').getall())
        if len(content) < 100:
            return
        title = response.css('h1::text').get()
        time_text = response.css('.post_time_source::text').get()
        timestamp_text = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', time_text).group()
        timestamp = datetime.fromisoformat(timestamp_text)
        category = response.css('.post_crumb a::text').getall()[-1]
        Post.objects.create(
            title=title,
            timestamp=timestamp,
            category=category,
            content=content,
            url=response.url
        )
        print(title)

# -*- coding: utf-8 -*-

import hashlib
import yaml

from scrapy import signals


class SaveStatistics(object):
    def __init__(self, crawler):
        self.stats = crawler.stats
        self.MONGO = crawler.settings.get('MONGO')

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        instance = cls(crawler)
        crawler.signals.connect(instance.spider_closed, signal=signals.spider_closed)
        return instance

    def spider_closed(self, spider, reason):
        dumppy_stats = self.stats.get_stats()
        scraped_num = dumppy_stats.get('item_scraped_count', 0)
        if scraped_num > 0 and hasattr(spider, 'statistics'):
            info = {}
            info['name'] = spider.name
            urls = set(i['spider_url'] for i in spider.statistics)
            info['urls'] = yaml.safe_dump(urls)
            info['hash'] = hashlib.sha256(info['urls']).hexdigest()
            info['finish_reason'] = dumppy_stats.get('finish_reason')
            info['start_time'] = dumppy_stats.get('start_time')
            info['finish_time'] = dumppy_stats.get('finish_time')
            used_time = info['finish_time'] - info['start_time']
            info['used_time'] = used_time.total_seconds()
            info['scraped'] = scraped_num
            info['dropped'] = dumppy_stats.get('item_dropped_count', 0)
            info['errors'] = dumppy_stats.get('log_count/ERROR', 0)
            self.MONGO.statistics.insert_one(info)

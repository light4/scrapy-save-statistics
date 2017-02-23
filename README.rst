Save statistics extension for `Scrapy <http://scrapy.org/>`__
=============================================================

Save statistics to mongo for analytics.

Install
-------

The quick way:

::

    pip install scrapy-save-statistics

Or install from GitHub:

::

    pip install git+git://github.com/light4/scrapy-save-statistics.git@master

Or checkout the source and run:

::

    python setup.py install

settings.py
-----------

Mongodb settings for save statistics, need a *statistics* database.

::

    MONGO_HOST = "127.0.0.1"
    MONGO_PORT = 27017
    MONGO_DB = "myspider"
    MONGO_STATISTICS = "statistics"

    EXTENSIONS = {
        'scrapy_save_statistics.SaveStatistics': 100,
    }

Spider
-------

Spider must have *statistics* attributes and contains spider_url.
We'll save that info to mongodb.

::

    class TestSpider(scrapy.Spider):
        name = "test"

        def __init__(self, name=None, **kwargs):
            super(TestSpider, self).__init__(name=name, **kwargs)
            self.statistics = []

        def parse(self, response):
            crawl_info = {'spider_url': spider_url,
                          'expected_crawl_num': expected_crawl_num,
                          'pages': total_page}
            self.statistics.append(crawl_info)

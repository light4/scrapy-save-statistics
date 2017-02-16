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

    class MyMongo(object):
        def __init__(self, host="127.0.0.1", port=27017, db="myspider"):
            self.connection = pymongo.MongoClient(
                host=host,
                port=port
            )
            self.db = self.connection[db]
            data = [
                "bot",
                "test",
                "statistics",
            ]
            for item in data:
                setattr(self, item, self.db[item])


    MONGO = MyMongo()

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

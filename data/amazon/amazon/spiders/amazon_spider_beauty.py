import time

import scrapy
from ..items import AmazonItem


class AmazonSpiderBeauty(scrapy.Spider):
    name = 'amazon_spider_beauty'

    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&rh=n%3A16225006011&page=2&qid=1568750157&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?rh=n%3A16225006011&page=385']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A11058281&dc&page=386&fst=as%3Aoff&qid=1569603195&rnid=16225006011&ref=sr_pg_386']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A11060451&dc&page=267&fst=as%3Aoff&qid=1569614944&rnid=16225006011&ref=sr_pg_267']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A11057241&dc&page=2&fst=as%3Aoff&qid=1569615651&rnid=16225006011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A11056591&dc&page=2&fst=as%3Aoff&qid=1569616235&rnid=16225006011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A17242866011&dc&page=62&fst=as%3Aoff&qid=1569620079&rnid=16225006011&ref=sr_pg_62']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A11062741&dc&page=285&fst=as%3Aoff&qid=1569622463&rnid=16225006011&ref=sr_pg_284']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A3778591&dc&page=2&fst=as%3Aoff&qid=1569666720&rnid=16225006011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&dc&page=162&fst=as%3Aoff&qid=1569673192&rnid=16225006011&ref=sr_pg_162']
    start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&bbn=16225006011&rh=n%3A16225006011%2Cn%3A10079992011&dc&page=4&fst=as%3Aoff&qid=1569676120&rnid=16225006011&ref=sr_pg_2']

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        if next_page_real is not None:
            time.sleep(5)
            yield response.follow(next_page_real, callback=self.parse)

import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderHomeKitchen(scrapy.Spider):
    name = 'amazon_spider_home'

    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&rh=n%3A16225011011&page=2&qid=1568862873&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?rh=n%3A16225011011&page=100']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&rh=n%3A16225011011&page=110&qid=1568978621&ref=sr_pg_100']
    # start_urls = ['https://www.amazon.com/s?rh=n%3A16225011011&page=305']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&dc&page=214&fst=as%3Aoff&qid=1570052006&rnid=16225011011&ref=sr_pg_214']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A3206325011&dc&page=2&fst=as%3Aoff&qid=1570053403&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A284507&dc&page=2&fst=as%3Aoff&qid=1570056798&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A1063252&dc&page=2&qid=1570099362&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A10632363A1063236&dc&page=2&qid=1570111988&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A1063306&dc&page=310&qid=1570116993&rnid=16225011011&ref=sr_pg_310']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A1063278&dc&page=2&qid=1570117872&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A3736081&dc&page=363&qid=1570139235&rnid=16225011011&ref=sr_pg_363']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A16510975011&dc&page=2&qid=1570140259&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A13679381&dc&page=2&qid=1570142656&rnid=16225011011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A%2116225011011%2Cn%3A901590&dc&qid=1570085063&rnid=16225011011&ref=sr_nr_n_10']
    start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&bbn=16225011011&rh=n%3A16225011011%2Cn%3A3206324011&dc&page=161&qid=1570149029&rnid=16225011011&ref=sr_pg_161']

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
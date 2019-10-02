import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderHealthHousehold(scrapy.Spider):
    name = 'amazon_spider_health'
    # start_urls = [
    #     'https://www.amazon.com/s?i=hpc-intl-ship&rh=n%3A%2116225010011&page=2&qid=1568987308&ref=lp_16225010011_pg_2'
    # ]
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A10787321&dc&page=2&fst=as%3Aoff&qid=1569951259&rnid=16225010011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A3760941&dc&page=2&fst=as%3Aoff&qid=1569966488&rnid=16225010011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A15342811&dc&page=2&fst=as%3Aoff&qid=1569968963&rnid=16225010011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A3775161&dc&page=212&fst=as%3Aoff&qid=1569972265&rnid=16225010011&ref=sr_pg_212']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A3777371&dc&page=369&fst=as%3Aoff&qid=1570005521&rnid=16225010011&ref=sr_pg_369']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A6973663011&dc&page=2&fst=as%3Aoff&qid=1570006959&rnid=16225010011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A723418011&dc&page=2&fst=as%3Aoff&qid=1570018871&rnid=16225010011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A10079994011&dc&page=2&fst=as%3Aoff&qid=1570023235&rnid=16225010011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A3764441&dc&page=2&fst=as%3Aoff&qid=1570026803&rnid=16225010011&ref=sr_pg_2']
    start_urls = ['https://www.amazon.com/s?i=hpc-intl-ship&bbn=16225010011&rh=n%3A16225010011%2Cn%3A10079996011&dc&page=2&fst=as%3Aoff&qid=1570047551&rnid=16225010011&ref=sr_pg_2']

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

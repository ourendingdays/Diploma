import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderIndustrialScientific(scrapy.Spider):
    name = 'amazon_spider_industrial'

    start_urls = ['https://www.amazon.com/s?i=industrial-intl-ship&rh=n%3A%2116225012011&page=2&qid=1568990497&ref=lp_16225012011_pg_2']

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

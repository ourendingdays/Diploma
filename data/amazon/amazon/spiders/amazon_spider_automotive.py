import scrapy
from ..items import AmazonItem


class AmazonSpiderAutomotive(scrapy.Spider):
    name = 'amazon_spider_automotive'

    # start_urls = ['https://www.amazon.com/s?rh=n%3A2562090011&page=2&qid=1568730935&ref=lp_2562090011_pg_2']
    start_urls = ['https://www.amazon.com/Automotive/s?rh=n%3A2562090011&page=390']

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        if next_page_real is not None:
            yield response.follow(next_page_real, callback=self.parse)

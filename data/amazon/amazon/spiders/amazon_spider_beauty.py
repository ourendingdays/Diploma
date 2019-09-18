import scrapy
from ..items import AmazonItem


class AmazonSpiderBeauty(scrapy.Spider):
    name = 'amazon_spider_beauty'

    # start_urls = ['https://www.amazon.com/s?i=beauty-intl-ship&rh=n%3A16225006011&page=2&qid=1568750157&ref=sr_pg_2']
    start_urls = ['https://www.amazon.com/s?rh=n%3A16225006011&page=385']

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        if next_page_real is not None:
            yield response.follow(next_page_real, callback=self.parse)

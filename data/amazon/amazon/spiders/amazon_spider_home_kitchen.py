import scrapy
from ..items import AmazonItem


class AmazonSpiderHomeKitchen(scrapy.Spider):
    name = 'amazon_spider_home'

    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&rh=n%3A16225011011&page=2&qid=1568862873&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?rh=n%3A16225011011&page=100']
    # start_urls = ['https://www.amazon.com/s?i=kitchen-intl-ship&rh=n%3A16225011011&page=110&qid=1568978621&ref=sr_pg_100']
    start_urls = ['https://www.amazon.com/s?rh=n%3A16225011011&page=300']
    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        if next_page_real is not None:
            yield response.follow(next_page_real, callback=self.parse)

import scrapy
from ..items import AmazonItem


class AmazonSpiderArts(scrapy.Spider):
    name = 'amazon_spider_art'
    # start_urls = [
    #     'https://www.amazon.com/s?i=arts-crafts-intl-ship&rh=n%3A4954955011&qid=1568238763&ref=sr_pg_1'
    # ]
    # start_urls = [
    #     'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=53'
    # ]
    # start_urls = [
    #     'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=70'
    # ]
    start_urls = [
        'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=140'
    ]
    page_number = 141
    page_number_total = 400

    def parse(self, response):
        items = AmazonItem()
        # next_page_real = response.css('.a-last a').css('::attr(href)').extract()

        # this one takes all ads on a page
        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        next_page = 'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=' + str(AmazonSpiderArts.page_number)
        if AmazonSpiderArts.page_number <= AmazonSpiderArts.page_number_total:
            AmazonSpiderArts.page_number += 1
            yield response.follow(next_page, callback=self.parse)



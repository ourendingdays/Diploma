import scrapy
from ..items import AmazonItem


class AmazonSpiderComputers(scrapy.Spider):
    name = 'amazon_spider_computers'

    # start_urls = [
    #     'https://www.amazon.com/s?rh=n%3A16225007011&page=2&qid=1568446300&ref=lp_16225007011_pg_2'
    # ]
    # start_urls = [
    #     'https://www.amazon.com/s?i=computers-intl-ship&rh=n%3A16225007011&page=3&qid=1568446306&ref=sr_pg_3'
    # ]
    # start_urls = [
    #     'https://www.amazon.com/Computers/s?rh=n%3A16225007011&page=90'
    # ]
    start_urls = [
        'https://www.amazon.com/Computers/s?rh=n%3A16225007011&page=347'
    ]

    page_number = 316
    page_number_total = 400

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        # next_page = 'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=' + str(AmazonSpiderArts.page_number)
        # if AmazonSpiderArts.page_number <= AmazonSpiderArts.page_number_total:
        #     AmazonSpiderArts.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)

        if next_page_real is not None:
            yield response.follow(next_page_real, callback=self.parse)


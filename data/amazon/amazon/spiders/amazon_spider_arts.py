import time
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
    # start_urls = [
    #     'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=140'
    # ]
    # start_urls = [
    #     'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=200'
    # ]
    # start_urls = [
    #     'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=315'
    # ]
    # start_urls = ['https://www.amazon.com/Painting-Drawing-Art-Supplies/s?rh=n%3A2747968011&page=260']
    # start_urls = ['https://www.amazon.com/Beading-Jewelry-Making-Arts-Crafts-Sewing/s?rh=n%3A12896081&page=335']
    # start_urls = ['https://www.amazon.com/s?i=arts-crafts-intl-ship&bbn=4954955011&rh=n%3A4954955011%2Cn%3A2617942011%2Cn%3A378733011&dc&page=2&fst=as%3Aoff&qid=1569353553&rnid=2617942011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Fabric-Arts-Crafts-Sewing/s?rh=n%3A12899121&page=249']
    # start_urls = ['https://www.amazon.com/Fabric-Decorating-Arts-Crafts-Sewing/s?rh=n%3A12896841&page=220']
    # start_urls = ['https://www.amazon.com/s?i=arts-crafts-intl-ship&bbn=4954955011&rh=n%3A4954955011%2Cn%3A2617942011%2Cn%3A12897221&dc&page=2&fst=as%3Aoff&qid=1569415197&rnid=2617942011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Needlework-Arts-Crafts-Sewing/s?rh=n%3A2237329011&page=260']
    # start_urls = ['https://www.amazon.com/Organization-Storage-Transport-Arts-Crafts-Sewing/s?rh=n%3A2237594011&page=285']
    # start_urls = ['https://www.amazon.com/Printmaking-Arts-Crafts-Sewing/s?rh=n%3A12898451&page=344']
    # start_urls = ['https://www.amazon.com/s?i=arts-crafts-intl-ship&bbn=4954955011&rh=n%3A4954955011%2Cn%3A2617942011%2Cn%3A12898821&dc&page=2&fst=as%3Aoff&qid=1569438393&rnid=2617942011&ref=sr_pg_2']
    start_urls = ['https://www.amazon.com/s?i=arts-crafts-intl-ship&bbn=4954955011&rh=n%3A4954955011%2Cn%3A2617942011%2Cn%3A12899091&dc&page=2&fst=as%3Aoff&qid=1569441489&rnid=2617942011&ref=sr_pg_2']
    # page_number = 316
    # page_number_total = 400

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

        # next_page = 'https://www.amazon.com/Arts-Crafts/s?rh=n%3A4954955011&page=' + str(AmazonSpiderArts.page_number)
        # if AmazonSpiderArts.page_number <= AmazonSpiderArts.page_number_total:
        #     AmazonSpiderArts.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)
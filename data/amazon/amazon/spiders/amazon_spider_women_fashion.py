import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderWomenFashion(scrapy.Spider):
    name = 'amazon_spider_women'

    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1045024&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=e9a7a2cd-d373-460c-8c25-702b5e2acb03&pf_rd_r=8QEXM8WHY2N3V0TEP07X&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1569064421&rnid=1040660&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Dresses-Clothing/s?rh=n%3A1045024&page=270']
    start_urls = ['https://www.amazon.com/Tops-Tees-Blouses-Clothing/s?rh=n%3A2368343011&page=215']


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

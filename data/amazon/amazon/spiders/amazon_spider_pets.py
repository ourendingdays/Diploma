import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderPets(scrapy.Spider):
    name = 'amazon_spider_pets'

    # start_urls = [
    #     'https://www.amazon.com/s?i=pets-intl-ship&bbn=16225013011&rh=n%3A16225013011%2Cn%3A2975312011&dc&page=3&fst=as%3Aoff&pf_rd_i=16225013011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=840ea3ca-218c-4921-bdeb-ab06a7a27a3c&pf_rd_r=CN31HGPMYAJC96MZMTDV&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1568997582&rnid=16225013011&ref=sr_pg_2'
    # ]
    # start_urls = [
    #    'https://www.amazon.com/Dogs-Pet-Supplies/s?rh=n%3A2975312011&page=335'
    # ]
    # start_urls = [
    #    'https://www.amazon.com/s?i=pets-intl-ship&bbn=16225013011&rh=n%3A16225013011%2Cn%3A2975241011&dc&page=2&fst=as%3Aoff&pf_rd_i=16225013011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=840ea3ca-218c-4921-bdeb-ab06a7a27a3c&pf_rd_r=CN31HGPMYAJC96MZMTDV&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1568997415&rnid=16225013011&ref=sr_pg_2'
    # ]
    start_urls = [
       'https://www.amazon.com/s?i=pets-intl-ship&bbn=16225013011&rh=n%3A16225013011%2Cn%3A2975446011&dc&page=3&fst=as%3Aoff&pf_rd_i=16225013011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=840ea3ca-218c-4921-bdeb-ab06a7a27a3c&pf_rd_r=TNQZS6RDTE7XF194E62J&pf_rd_s=merchandised-search-2&pf_rd_t=101&qid=1569013158&rnid=16225013011&ref=sr_pg_2'
    ]

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

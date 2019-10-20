import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderToolsHome(scrapy.Spider):
    name = 'amazon_spider_tools'

    start_urls = ['https://www.amazon.com/s?i=fashion-girls&bbn=7581687011&rh=n%3A7141123011%2Cn%3A7147442011%2Cn%3A7581687011%2Cp_n_shipping_option-bin%3A3242350011&page=3&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=BAKH0MMRQ05K8WH30HZN&pf_rd_r=BAKH0MMRQ05K8WH30HZN&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571499263&ref=sr_pg_3']

    def parse(self, response):
        items = AmazonItem()

        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-size-base-plus::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]
            yield items

        if next_page_real is not None:
            time.sleep(2)
            yield response.follow(next_page_real, callback=self.parse)

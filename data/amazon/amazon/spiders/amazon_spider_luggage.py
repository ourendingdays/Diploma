import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderLuggage(scrapy.Spider):
    name = 'amazon_spider_luggage'

    # start_urls = ['https://www.amazon.com/s?i=luggage-intl-ship&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A15743261&page=2&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570611140&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=luggage-intl-ship&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A360832011&page=2&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570611970&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A15743271&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743241&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A15743291&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A9971584011&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A2477388011&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743251%2Cn%3A2477386011&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnavn']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743231&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    # start_urls = ['https://www.amazon.com/s?i=luggage-intl-ship&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15744111&page=6&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570621166&ref=sr_pg_6']
    # start_urls = ['https://www.amazon.com/s?bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743211&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&ref=AE_Luggage_leftnav']
    start_urls = ['https://www.amazon.com/s?i=luggage-intl-ship&bbn=16225017011&rh=n%3A7141123011%2Cn%3A16225017011%2Cn%3A15743971&page=185&pf_rd_i=16225017011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_p=92f6b9f6-45a8-4a56-916b-6d695966ee4a&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_r=D40Y8KK0Y171CM653RSC&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570636637&ref=sr_pg_185']

    def parse(self, response):
        items = AmazonItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-size-base-plus::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]
            yield items

        if next_page_real is not None:
            time.sleep(5)
            yield response.follow(next_page_real, callback=self.parse)

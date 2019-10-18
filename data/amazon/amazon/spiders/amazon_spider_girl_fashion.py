import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderGirlFashion(scrapy.Spider):
    name = 'amazon_spider_girl'
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A3455761&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1288617011&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045470&dc&page=177&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571386992&rnid=1040664&ref=sr_pg_177']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A5604818011&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045206&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045268&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A5468988011&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A2412731011&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045272&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045264&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045266&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_11']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045468&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_12']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045424&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_13']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045426&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_14']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A3455741&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_15']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A3455751&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_16']
    # start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1044490&dc&page=119&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571421799&rnid=1040664&ref=sr_pg_119']
    start_urls = ['https://www.amazon.com/s?i=fashion-girls-intl-ship&bbn=16225020011&rh=n%3A16225020011%2Cn%3A1040664%2Cn%3A1045428&dc&pf_rd_i=16225020011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_p=590edd7e-7bd2-4b3d-b0e0-acc975fc0961&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_r=Z94X4YZ5PZ2K7RXMH23D&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571382166&rnid=1040664&ref=sr_nr_n_18']



















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
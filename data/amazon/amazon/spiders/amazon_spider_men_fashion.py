import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderMenFashion(scrapy.Spider):
    name = 'amazon_spider_men'

    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A2476517011&dc&page=345&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571143523&rnid=1040658&ref=sr_pg_345']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1258644011&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571128087&rnid=1040658&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1044442&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571128087&rnid=1040658&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045830&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571128087&rnid=1040658&ref=sr_nr_n_4v']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045564&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571128087&rnid=1040658&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045558&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571156154&rnid=1040658&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045560&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571156154&rnid=1040658&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A3455821&dc&page=364&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571169569&rnid=1040658&ref=sr_pg_364']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1046670&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571156154&rnid=1040658&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045684&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571156154&rnid=1040658&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045706&dc&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571156154&rnid=1040658&ref=sr_nr_n_11']
    start_urls = ['https://www.amazon.com/s?i=fashion-mens-intl-ship&bbn=16225019011&rh=n%3A16225019011%2Cn%3A1040658%2Cn%3A1045708&dc&page=131&pf+_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_i=16225019011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_p=5cd8272b-5ce4-4c26-bfcb-d6dca0c1e427&pf_rd_r=DP43KQH5Z5M7HFC5R7A8&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1571175447&rnid=1040658&ref=sr_pg_131']

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
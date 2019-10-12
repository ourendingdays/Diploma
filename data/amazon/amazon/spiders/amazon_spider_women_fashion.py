import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderWomenFashion(scrapy.Spider):
    name = 'amazon_spider_women'

    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1045024&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=e9a7a2cd-d373-460c-8c25-702b5e2acb03&pf_rd_r=8QEXM8WHY2N3V0TEP07X&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1569064421&rnid=1040660&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Dresses-Clothing/s?rh=n%3A1045024&page=270']
    # start_urls = ['https://www.amazon.com/Tops-Tees-Blouses-Clothing/s?rh=n%3A2368343011&page=215']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1044456&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=e9a7a2cd-d373-460c-8c25-702b5e2acb03&pf_rd_r=8QEXM8WHY2N3V0TEP07X&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1569100636&rnid=1040660&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Fashion-Hoodies-Sweatshirts-Clothing/s?rh=n%3A1258603011&page=235']
    # start_urls = ['https://www.amazon.com/Jeans-Clothing/s?rh=n%3A1048188&page=110']
    # start_urls = ['https://www.amazon.com/Pants-Clothing/s?rh=n%3A1048184&page=310']
    # start_urls = ['https://www.amazon.com/Skirts-Clothing/s?rh=n%3A1045022&page=377']
    # start_urls = ['https://www.amazon.com/Shorts-Clothing/s?rh=n%3A1048186&page=293']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A1258967011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=e9a7a2cd-d373-460c-8c25-702b5e2acb03&pf_rd_r=8QEXM8WHY2N3V0TEP07X&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1569181277&rnid=1040660&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A3456051&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=4QH1R4R5T751ZQ1FKQAW&pf_rd_r=4QH1R4R5T751ZQ1FKQAW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1569228522&rnid=1040660&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Swimsuits-Cover-Ups-Clothing/s?rh=n%3A1046622&page=190']
    # start_urls = ['https://www.amazon.com/Lingerie-Sleep-Lounge-Clothing/s?rh=n%3A9522931011&page=270']
    # start_urls = ['https://www.amazon.com/Jumpsuits-Rompers-Overalls-Clothing/s?rh=n%3A9522930011&page=355']
    # start_urls = ['https://www.amazon.com/Coats-Jackets-Vests-Clothing/s?rh=n%3A1044646&page=275']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A1040660%2Cn%3A9522932011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=4QH1R4R5T751ZQ1FKQAW&pf_rd_r=4QH1R4R5T751ZQ1FKQAW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1569270810&rnid=1040660&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/Socks-Hosiery-Clothing/s?rh=n%3A1044886&page=255']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A7141123011%2Cn%3A16225018011%2Cn%3A1040660&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=7YWR4MMQ0JXW2JFXPGQ9&pf_rd_r=7YWR4MMQ0JXW2JFXPGQ9&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1569277142&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A6127771011&dc&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570790472&rnid=679337011&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679380011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570793471&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679394011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570808299&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%%3A3A16225018011%2Cn%3A679337011%2Cn%3A679399011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570875893&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679404011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570877750&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679410011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570878811&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A6127767011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570880275&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679415011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570881818&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679416011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570882525&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679425011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570890243&rnid=679337011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679433011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570897053&rnid=679337011&ref=sr_pg_2']
    start_urls = ['https://www.amazon.com/s?i=fashion-womens-intl-ship&bbn=16225018011&rh=n%3A16225018011%2Cn%3A679337011%2Cn%3A679442011&dc&page=2&pf_rd_i=16225018011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_p=0909843d-7d3a-40a7-8b35-6c3da8755bbd&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_r=28TCGP4Q4HJN0G7G31XW&pf_rd_s=merchandised-search-left-2&pf_rd_t=101&qid=1570898569&rnid=679337011&ref=sr_pg_2']

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

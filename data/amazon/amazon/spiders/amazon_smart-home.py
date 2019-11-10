import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderSmartHome(scrapy.Spider):
    name = 'amazon_smart-home'

    start_urls = ['https://www.amazon.com/s?i=specialty-aps&srs=13575748011&page=2&qid=1573325754&ref=lp_13575748011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=16334612011&page=2&qid=1573325695&ref=lp_16334612011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=16713337011&page=2&qid=1573325874&ref=lp_16713337011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=13575750011&page=2&qid=1573325897&ref=lp_13575750011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=16334613011&page=2&qid=1573325920&ref=lp_16334613011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=13575749011&page=2&qid=1573325941&ref=lp_13575749011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=18447749011&page=2&qid=1573325978&ref=lp_18447749011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=16713338011&page=2&qid=1573326009&ref=lp_16713338011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=17284462011&page=2&qid=1573326029&ref=lp_17284462011_pg_2',
                  'https://www.amazon.com/b/ref=amb_link_14?ie=UTF8&node=19185102011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=FQBG6DCMWXQG3P8GW8RD&pf_rd_r=FQBG6DCMWXQG3P8GW8RD&pf_rd_t=101&pf_rd_p=b3eda132-d776-482d-b2d8-32b48acf2fec&pf_rd_p=b3eda132-d776-482d-b2d8-32b48acf2fec&pf_rd_i=13575748011',
                  'https://www.amazon.com/s?i=specialty-aps&srs=17934444011&page=2&qid=1573326093&ref=lp_17934444011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=19185103011&page=2&qid=1573326112&ref=lp_19185103011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=18653614011&page=2&qid=1573326134&ref=lp_18653614011_pg_2',
                  'https://www.amazon.com/s?i=specialty-aps&srs=19185106011&page=2&qid=1573326153&ref=lp_19185106011_pg_2']

    def parse(self, response):
        items = AmazonItem()

        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]
            yield items

        if next_page_real is not None:
            time.sleep(2)
            yield response.follow(next_page_real, callback=self.parse)

import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderBaby(scrapy.Spider):
    name = 'amazon_spider_baby'

    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A%2116225005011%2Cn%3A239225011&dc&fst=as%3Aoff&qid=1570637625&rnid=16225005011&ref=lp_16225005011_nr_n_0']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A7147444011&dc&page=2&fst=as%3Aoff&qid=1570647384&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A196601011&dc&page=320&fst=as%3Aoff&qid=1570657758&rnid=16225005011&ref=sr_pg_320']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A17720255011&dc&page=2&fst=as%3Aoff&qid=1570658259&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A%2116225005011%2Cn%3A405369011&dc&fst=as%3Aoff&qid=1570660784&rnid=16225005011&ref=lp_16225005011_nr_n_4']
    start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A%2116225005011%2Cn%3A166835011&dc&fst=as%3Aoff&qid=1570660784&rnid=16225005011&ref=lp_16225005011_nr_n_5']

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

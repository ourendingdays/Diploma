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
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A%2116225005011%2Cn%3A166835011&dc&fst=as%3Aoff&qid=1570660784&rnid=16225005011&ref=lp_16225005011_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A166764011&dc&page=2&fst=as%3Aoff&qid=1570693876&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A166777011&dc&page=2&fst=as%3Aoff&qid=1570696215&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A239226011&dc&page=2&fst=as%3Aoff&qid=1570698846&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A695338011&dc&page=301&fst=as%3Aoff&qid=1570703640&rnid=16225005011&ref=sr_pg_301']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A166887011&dc&page=2&fst=as%3Aoff&qid=1570716162&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A166804011&dc&page=2&fst=as%3Aoff&qid=1570716221&rnid=16225005011&ref=sr_pg_2']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A166863011&dc&page=185&fst=as%3Aoff&qid=1570718985&rnid=16225005011&ref=sr_pg_185']
    # start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A8446318011&dc&page=2&fst=as%3Aoff&qid=1570782667&rnid=16225005011&ref=sr_pg_2']
    start_urls = ['https://www.amazon.com/s?i=baby-products-intl-ship&bbn=16225005011&rh=n%3A16225005011%2Cn%3A17726796011&dc&page=2&fst=as%3Aoff&qid=1570784355&rnid=16225005011&ref=sr_pg_2']

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

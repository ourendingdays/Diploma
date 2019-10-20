import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderToolsHome(scrapy.Spider):
    name = 'amazon_spider_tools'

    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A19149191011&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741261&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741271&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741331&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A13399891&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741441&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741411&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741161&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741361&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A2383576011&dc&fst=as%3Aoff&qid=1571565875&rnid=13397451&ref=sr_nr_n_13']
    start_urls = ['https://www.amazon.com/s?i=tools-intl-ship&bbn=256643011&rh=n%3A256643011%2Cn%3A%21468240%2Cn%3A13397451%2Cn%3A3741521&dc&fst=as%3Aoff&qid=1571596356&rnid=13397451&ref=sr_nr_n_14']















































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

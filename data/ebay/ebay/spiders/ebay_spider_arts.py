# -*- coding: utf-8 -*-
import scrapy
from ..items import EbayItem


class EbaySpiderArts(scrapy.Spider):
    name = 'ebay_spider_arts'
    start_urls = ['https://www.amazon.com/s?rh=n%3A16225009011&page=45']

    def parse(self, response):
        items = EbayItem()
        next_page_real = response.css(".a-last a").css("::attr(href)").get()

        ad = response.css('.a-color-base.a-text-normal::text').extract()

        for i in range(len(ad)):
            items['ad'] = ad[i]

            yield items

        if next_page_real is not None:
            yield response.follow(next_page_real, callback=self.parse)
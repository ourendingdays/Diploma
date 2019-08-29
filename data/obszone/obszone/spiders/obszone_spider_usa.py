import scrapy
from ..items import ObszoneItem


# inheriting from class scrapy.Spider
class ObszoneSpider(scrapy.Spider):
    name = 'obszone_spider_usa'

    # list of websites we want to scrap
    start_urls = ['https://www.obszone.com/free-ads/new-york-city/5128581']

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        # an instance variable
        item = ObszoneItem()

        articles = response.css(".item-list")
        next_page = response.css(".page-item:nth-child(7) .page-link::attr(href)").get()

        for article in articles:
            ad = article.css(".add-title a::text").extract()

            item['ad'] = ad
            # yield = return
            # yield works with generator
            yield item

        if next_page is not None:
            # callback tells Scrapy what to do next
            yield response.follow(next_page, callback=self.parse)


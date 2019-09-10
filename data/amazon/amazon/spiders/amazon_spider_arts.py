import scrapy
from ..items import AmazonItem


# inheriting from class scrapy.Spider
class GeeboSpiderVehicles(scrapy.Spider):
    name = 'geebo_spider_vehicles'
    page_number = 2
    # site has 50 pages of equipment
    page_number_total = 50

    # list of websites we want to scrap
    start_urls = ['https://geebo.com/vehicles/list/mobile//page/1/']

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        # an instance variable
        item = AmazonItem()

        articles = response.css(".image+ td")
        next_page = 0

        for article in articles:
            ad = article.css(".title::text").extract()
            # ad_href = article.css(".title::attr(href)").get()
            # print('ad_href: ', ad_href)

            item['ad'] = ad

            # yield = return
            # yield works with generator
            yield item

        if next_page is not None:
            # callback tells Scrapy what to do next
            yield response.follow(next_page, callback=self.parse)
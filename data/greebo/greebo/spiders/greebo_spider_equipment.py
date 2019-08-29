import scrapy
from ..items import GreeboItem


# inheriting from class scrapy.Spider
class GreeboSpiderEquipment(scrapy.Spider):
    name = 'greebo_spider_equipment'
    page_number = 2
    # site has 50 pages of equipment
    page_number_total = 50

    # list of websites we want to scrap
    start_urls = ['https://geebo.com/construction-farm-equipment/list/mobile//page/1/']

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        # an instance variable
        item = GreeboItem()

        articles = response.css(".image+ td")
        next_page = response.css(".paging a::attr(href)").get()

        for article in articles:
            ad = article.css(".title::text").extract()
            ad_href = article.css(".title::attr(href)").get()
            print('ad_href: ', ad_href)

            item['ad'] = ad

            # yield = return
            # yield works with generator
            yield item

        next_page = 'https://geebo.com/construction-farm-equipment/list/mobile//page/' + str(GreeboSpiderEquipment.page_number) + '/'
        if GreeboSpiderEquipment.page_number <= GreeboSpiderEquipment.page_number_total:
            GreeboSpiderEquipment.page_number += 1
            # callback tells Scrapy what to do next
            yield response.follow(next_page, callback=self.parse)

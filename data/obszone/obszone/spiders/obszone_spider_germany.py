import scrapy
from ..items import ObszoneItem


# inheriting from class scrapy.Spider
class ObszoneSpider(scrapy.Spider):
    name = 'obszone_spider_germany'
    page_number = 2

    # list of websites we want to scrap
    start_urls = ['https://www.obszone.com/search?_token=Gps9XyufdMf0MJA74P4q0VGCG8jtV4NOikfoE4Nf&type=1'
                  ]

    # response contains a source code of the web page we are scrapping (from start_url)
    def parse(self, response):
        # an instance variable
        item = ObszoneItem()

        articles = response.css(".item-list")
        next_page = response.css(".page-item:nth-child(6) .page-link::attr(href)").get()
        print('NEXT PAGE: ', next_page)

        for article in articles:
            ad = article.css(".add-title a::text").extract()
            ad_href = article.css(".add-title a::attr(href)").get()
            print('ad_href: ', ad_href)

            item['ad'] = ad

            # yield = return
            # yield works with generator
            yield item

        if next_page is not None:
            # callback tells Scrapy what to do next
            yield response.follow(next_page, callback=self.parse)

        # next_page = 'https://www.obszone.com/search?_token=Gps9XyufdMf0MJA74P4q0VGCG8jtV4NOikfoE4Nf&type=1&page=' + str(ObszoneSpider.page_number)
        # if ObszoneSpider.page_number < 4:
        #     print('NEXT_PAGE is: ', next_page)
        #     ObszoneSpider.page_number += 1
        #     # callback tells Scrapy what to do next
        #     yield response.follow(next_page, callback=self.parse)
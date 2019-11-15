import scrapy
from ..items import AmazonItem
import time


class AmazonSpiderSmartHome(scrapy.Spider):
    name = 'amazon_sports-outdoors'

    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11443874011&dc&fst=as%3Aoff&qid=1573327259&rnid=706814011&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3400391&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A10208056011&dc&page=155&fst=as%3Aoff&qid=1573331408&rnid=3400371&ref=sr_pg_155']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3401611&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A2204505011&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3400781&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A2371054011&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A2204475011&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A2204506011&dc&page=375&fst=as%3Aoff&qid=1573337447&rnid=3400371&ref=sr_pg_375']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3400851&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3401301&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A10208058011&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_11']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3401541&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_12']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3401081&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_13']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3400371%2Cn%3A3401281&dc&fst=as%3Aoff&qid=1573329093&rnid=3400371&ref=sr_nr_n_14']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3402401&dc&fst=as%3Aoff&qid=1573327259&rnid=706814011&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A3403201&dc&fst=as%3Aoff&qid=1573327259&rnid=706814011&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051398011&dc&fst=as%3Aoff&qid=1573327259&rnid=706814011&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A706814011%2Cn%3A11051400011&dc&page=109&fst=as%3Aoff&qid=1573353371&ref=sr_pg_109']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A2204518011%2Cn%3A3416451&dc&fst=as%3Aoff&qid=1573355206&rnid=2204518011&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A706814011%2Cn%3A2204518011%2Cn%3A2342470011&dc&page=269&fst=as%3Aoff&qid=1573356475&rnid=2204518011&ref=sr_pg_269']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A706814011%2Cn%3A2204518011%2Cn%3A2342471011&dc&page=282&fst=as%3Aoff&qid=1573395904&rnid=2204518011&ref=sr_pg_282']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A2204518011%2Cn%3A3417681&dc&fst=as%3Aoff&qid=1573818266&rnid=2204518011&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A2204518011%2Cn%3A2342472011&dc&fst=as%3Aoff&qid=1573818266&rnid=2204518011&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A2345540011&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A3406281&dc&page=328&fst=as%3Aoff&qid=1573820702&rnid=11051399011&ref=sr_pg_328']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A2345546011&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A3204434011&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A3418471&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A4201151&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A3421611&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A19614711011&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_9']
    start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A10208053011&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_10']



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

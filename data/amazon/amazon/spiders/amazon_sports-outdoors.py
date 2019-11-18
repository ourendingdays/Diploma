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
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A706814011%2Cn%3A11051399011%2Cn%3A10208053011&dc&fst=as%3Aoff&qid=1573819084&rnid=11051399011&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3421331%2Cn%3A3397331&dc&fst=as%3Aoff&qid=1573832383&rnid=3421331&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3421331%2Cn%3A11030588011&dc&fst=as%3Aoff&qid=1573832383&rnid=3421331&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3421331%2Cn%3A3399161&dc&fst=as%3Aoff&qid=1573832383&rnid=3421331&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A11444071011&dc&fst=as%3Aoff&qid=1573831958&rnid=10971181011&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3408061&dc&fst=as%3Aoff&qid=1573837271&rnid=3407731&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3407851&dc&fst=as%3Aoff&qid=1573838001&rnid=3407731&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3408021&dc&fst=as%3Aoff&qid=1573838001&rnid=3407731&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3407741&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3416071&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A5819907011&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3408271&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A11056111&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_11']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3422251&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_12']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A3407841&dc&fst=as%3Aoff&qid=1573843713&rnid=3407731&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A5393952011&dc&fst=as%3Aoff&qid=1573920677&rnid=3407731&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3407731%2Cn%3A1260445011&dc&fst=as%3Aoff&qid=1573922046&rnid=3407731&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3410851&dc&fst=as%3Aoff&qid=1573831958&rnid=10971181011&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706813011%2Cn%3A3412851&dc&fst=as%3Aoff&qid=1573929915&rnid=706813011&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706813011%2Cn%3A3408951&dc&fst=as%3Aoff&qid=1573931324&rnid=706813011&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706813011%2Cn%3A3395321&dc&fst=as%3Aoff&qid=1573931324&rnid=706813011&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3422351&dc&fst=as%3Aoff&qid=1573936836&rnid=10971181011&ref=sr_nr_n_15']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706815011&dc&fst=as%3Aoff&qid=1573937718&rnid=10971181011&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A10971181011%2Cn%3A706808011&dc&page=69&fst=as%3Aoff&qid=1573940526&rnid=10971181011&ref=sr_pg_69']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3416071%2Cn%3A2371056011&dc&fst=as%3Aoff&qid=1573982077&rnid=3416071&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3416071%2Cn%3A2226243011&dc&fst=as%3Aoff&qid=1573983655&rnid=3416071&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3416071%2Cn%3A617647011&dc&fst=as%3Aoff&qid=1573985019&rnid=3416071&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3416071%2Cn%3A3400551&dc&fst=as%3Aoff&qid=1573985019&rnid=3416071&ref=sr_nr_n_4']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3416071%2Cn%3A3395071&dc&fst=as%3Aoff&qid=1573985019&rnid=3416071&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3416071%2Cn%3A672097011&dc&fst=as%3Aoff&qid=1573985019&rnid=3416071&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3418761&dc&fst=as%3Aoff&qid=1573986556&rnid=10971181011&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A19574751011&dc&fst=as%3Aoff&qid=1573988176&rnid=706809011&ref=sr_nr_n_1']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3396541&dc&fst=as%3Aoff&qid=1573988176&rnid=706809011&ref=sr_nr_n_2']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3410221&dc&fst=as%3Aoff&qid=1573988176&rnid=706809011&ref=sr_nr_n_3']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A16225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3417981&dc&page=338&fst=as%3Aoff&qid=1573993399&rnid=706809011&ref=sr_pg_338']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A19574775011&dc&fst=as%3Aoff&qid=1573988176&rnid=706809011&ref=sr_nr_n_5']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A706816011&dc&fst=as%3Aoff&qid=1573988176&rnid=706809011&ref=sr_nr_n_6']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3414361&dc&fst=as%3Aoff&qid=1573988176&rnid=706809011&ref=sr_nr_n_7']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3412421&dc&fst=as%3Aoff&qid=1573998324&rnid=706809011&ref=sr_nr_n_8']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3412011&dc&fst=as%3Aoff&qid=1573998796&rnid=706809011&ref=sr_nr_n_9']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3420921&dc&fst=as%3Aoff&qid=1573998972&rnid=706809011&ref=sr_nr_n_10']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3407321&dc&fst=as%3Aoff&qid=1573998972&rnid=706809011&ref=sr_nr_n_11']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A3422351&dc&fst=as%3Aoff&qid=1574002000&rnid=706809011&ref=sr_nr_n_12']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A12119414011&dc&fst=as%3Aoff&qid=1574033919&rnid=706809011&ref=sr_nr_n_13']
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706809011%2Cn%3A12119428011&dc&fst=as%3Aoff&qid=1574034207&rnid=706809011&ref=sr_nr_n_14']
    # start_urls = [
    #     'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706810011%2Cn%3A3400051&dc&fst=as%3Aoff&qid=1574064916&rnid=706810011&ref=sr_nr_n_1',
    #     'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706810011%2Cn%3A13285461&dc&fst=as%3Aoff&qid=1574064916&rnid=706810011&ref=sr_nr_n_2',
    #     'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706810011%2Cn%3A13286711&dc&fst=as%3Aoff&qid=1574064916&rnid=706810011&ref=sr_nr_n_4',
    #     'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706810011%2Cn%3A3416451&dc&fst=as%3Aoff&qid=1574064916&rnid=706810011&ref=sr_nr_n_6',
    #     'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A706810011%2Cn%3A3415011&dc&fst=as%3Aoff&qid=1574064916&rnid=706810011&ref=sr_nr_n_7',
    # ]
    # start_urls = ['https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A10971181011%2Cn%3A3418761&dc&fst=as%3Aoff&qid=1574066058&rnid=10971181011&ref=sr_nr_n_9']
    start_urls = [
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A3209250011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_22',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A375519011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_21',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A374783011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_19',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A3250697011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_17',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A5769002011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_16',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A374893011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_15',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A2309018011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_14',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A374916011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_13',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A374819011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_12',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A374773011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_1',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A5768995011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_3',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A5768574011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_2',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A3209246011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_4',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A2311740011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_7',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A18882554011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_8',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A374747011&dc&fst=as%3Aoff&qid=1574067414&rnid=3386071&ref=sr_nr_n_9',
        'https://www.amazon.com/s?i=sporting-intl-ship&bbn=16225014011&rh=n%3A%2116225014011%2Cn%3A3386071%2Cn%3A2309443011&dc&fst=as%3Aoff&qid=1574067360&rnid=3386071&ref=sr_nr_n_20'
    ]








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

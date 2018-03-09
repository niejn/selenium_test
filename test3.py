import scrapy
from selenium import webdriver

class ProductSpider(scrapy.Spider):
    name = "product_spider"
    allowed_domains = ['ebay.com']
    start_urls = ['http://www.shfe.com.cn/data/dailydata/kx/pm20180301.dat']

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        self.driver.get(response.url)

        while True:
            next = self.driver.find_element_by_xpath('//td[@class="pagn-next"]/a')

            try:
                next.click()

                # get the data and write it to scrapy items
            except:
                break

        self.driver.close()
# from selenium import webdriver
import scrapy
from scrapy import Request
from selenium import webdriver
class northshoreSpider(scrapy.Spider):
    name = 'xxx'
    allowed_domains = ['www.example.org']
    start_urls = ['https://www.example.org']

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self,response):
            self.driver.get('https://www.example.org/abc')

            while True:
                try:
                    next = self.driver.find_element_by_xpath('//*[@id="BTN_NEXT"]')
                    url = 'http://www.example.org/abcd'
                    yield Request(url,callback=self.parse2)
                    next.click()
                except:
                    break

            self.driver.close()

    def parse2(self,response):
        print('you are here!')
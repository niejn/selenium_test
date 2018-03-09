# class spider(BaseSpider):
#     name = 'RubiGuesst'
#     start_urls = ['http://www.rubin-kazan.ru/guestbook.html']
#
#
# def parse(self, response):
#     url_list_gb_messages = re.search(r'url_list_gb_messages="(.*)"', response.body).group(1)
#     yield FormRequest('http://www.rubin-kazan.ru' + url_list_gb_messages, callback=self.RubiGuessItem,
#                       formdata={'page': str(page + 1), 'uid': ''})
#
#
# def RubiGuessItem(self, response):
#     json_file = response.body
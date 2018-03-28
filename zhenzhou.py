# <form name=form2 action="/cms/QueryTradeHolding" target="_blank" method="post">

'''

querytype:tradeamt
year:2018
bmonth:1
emonth:1
classid:SF
'''


from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from urllib.request import urlopen
import json
# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')

# html = urlopen("http://www.cffex.com.cn/sj/ccpm/201803/09/IF.xml")
# data = html.read()
# print(data)
# str_data = bytes.decode(data)
# j = json.loads(str_data)
# print(j)
# print(html.read())
# html = urlopen("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm")



# values = {
#     'querytype': 'tradeamt',
#     'memberDealPosiQuotes.trade_type': '0',
#     'year': '2018',
#     'bmonth': '2',
#     'emonth': '09',
#     'contract.contract_id': 'all',
#     'contract.variety_id': 'b',
# }
#
# # data = urlencode(values)
# url = "http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html"
#
# data = urlencode(values).encode(encoding='UTF8')
# request = Request(url, data)
#
# response = urlopen(request, timeout=4)
# re_data = response.read()
# re_data = re_data.decode('utf8')
#
# print(re_data)
#   # 转成dict数据，输出看看
# # print(data)


from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm")

sleep(1000)
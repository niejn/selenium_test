from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json

# html = urlopen("http://www.shfe.com.cn/data/dailydata/kx/pm20180307.dat")

'''
memberDealPosiQuotes.variety:b
memberDealPosiQuotes.trade_type:0
year:2018
month:2
day:09
contract.contract_id:all
contract.variety_id:b
'''

values = {
    'memberDealPosiQuotes.variety': 'b',
    'memberDealPosiQuotes.trade_type': '0',
    'year': '2018',
    'month': '2',
    'day': '09',
    'contract.contract_id': 'all',
    'contract.variety_id': 'b',
}

# data = urlencode(values)
url = "http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html"

data = urlencode(values).encode(encoding='UTF8')
request = Request(url, data)

response = urlopen(request, timeout=4)
re_data = response.read()
re_data = re_data.decode('utf8')

print(re_data)
  # 转成dict数据，输出看看
# print(data)

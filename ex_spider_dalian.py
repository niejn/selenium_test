from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from io import StringIO, BytesIO
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
'''
memberDealPosiQuotes.variety: b
memberDealPosiQuotes.trade_type: 0
year: 
month: 
day: 
contract.contract_id: all
contract.variety_id: b
'''

values = {
    'memberDealPosiQuotes.variety': 'b',
    'memberDealPosiQuotes.trade_type': '0',
    'year': '2018',
    'month': '5',
    'day': '11',
    'contract.contract_id': 'all',
    'contract.variety_id': 'b',
}

headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',

        # 'Host': 'www.shfe.com.cn',
        'Referer': 'http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rxq/index.html',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',

    }

import requests
url = "http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html"
session = requests.Session()
session.headers.update(headers)
s = session.get("http://www.dce.com.cn/dalianshangpin/xqsj/tjsj26/rtj/rcjccpm/index.html")
print(s.headers)
s = session.post(url, values)
print(s.headers)
# s.encoding = 'gbk'
print(s.text)
with open("dalian_res.txt", 'w') as da:
    da.write(s.text)
from lxml import html
from lxml import etree
tree = etree.HTML(s.text)
table = tree.xpath('//div/table')[1]
res = etree.tostring(table, encoding='gbk')
print(res)



parser = etree.HTMLParser()
tree   = etree.parse(StringIO(s.text), parser)
# tree = etree.fromstring(s.text)
# tree = html.parse(url, parser=parser)
# //*[@id="printData"]/div/table[2]
table = tree.findall('//*[@id="printData"]/div/table[2]')[0]
#  'lxml.etree._Element' object has no attribute 'tostring'
# result = table.tostring(html, pretty_print=True, method="html")
print()
data = [
    [td.text for td in row.findall('td')]
    for row in table.findall('tr')
    ]





url = "http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html"
# http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html
data = urlencode(values).encode(encoding='UTF8')
request = Request(url, data)

response = urlopen(request,)
re_data = response.read()
re_data = re_data.decode('utf8')

print(re_data)
  # 转成dict数据，输出看看
print(data)
# print(s.cookies.get_dict())
from lxml import html
from lxml import etree
from io import StringIO, BytesIO
tree = etree.fromstring(re_data)
# tree = html.parse(url, parser=parser)
table = tree.findall('//table')[1]
data = [
    [td.text_content().strip() for td in row.findall('td')]
    for row in table.findall('tr')
    ]
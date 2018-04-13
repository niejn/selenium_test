# Request URL: http://www.cffex.com.cn/sj/ccpm/201804/09/IF.xml
# Request Method: GET
# Status Code: 200 OK (from disk cache)
# Remote Address: 116.228.92.1:80
# Referrer Policy: no-referrer-when-downgrade
import datetime
from time import sleep

import requests

from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import xml.etree.ElementTree as ET
import io
'''
Accept: text/plain, */*; q=0.01
Referer: http://www.cffex.com.cn/ccpm/
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
X-Requested-With: XMLHttpRequest
'''
def main():




    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',

        # 'Host': 'www.shfe.com.cn',
        'Referer': 'http://www.cffex.com.cn/ccpm/',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',

    }
    # params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
    # url = 'http://www.shfe.com.cn/data/instrument/ContractBaseInfo20180321.dat'
    # url = "http://www.shfe.com.cn/data/dailydata/kx/kx20180319.dat"
    url = "http://www.cffex.com.cn/sj/ccpm/201804/09/IF.xml"
    # http://www.shfe.com.cn/data/dailydata/kx/pm20180327.dat
    # http://www.shfe.com.cn/data/instrument/ContractDailyTradeArgument20180321.dat
    request = requests.get(url, headers=headers)

    print(request.request.headers)
    # tree = html.fromstring(request.content)
    # xml_data = request.text
    xml_data = io.StringIO(request.text)
    etree = ET.parse(xml_data)  # create an ElementTree object
    # etree = ET.fromstring(xml_data)
    df = pd.DataFrame(list(etree))
    print(df)
    # doc_df = pd.DataFrame(list(iter_docs(etree.getroot())))
    # print(request.headers)
    # response = urlopen(request, timeout=4)
    # re_data = response.read()
    # re_data = re_data.decode('utf8')






    return

if __name__ == '__main__':
    main()
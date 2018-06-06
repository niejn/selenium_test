import xml
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from urllib.request import urlopen
import json
import requests
import json
import pandas as pd
from bs4 import BeautifulSoup
from lxml import html
import xml.etree.ElementTree as ET
import io
# http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180522/FutureDataHolding.htm

def html_parse():
    from lxml import html

    tree = html.parse('http://www.datamystic.com/timezone/time_zones.html')
    table = tree.findall('//table')[1]
    data = [
        [td.text_content().strip() for td in row.findall('td')]
        for row in table.findall('tr')
    ]
    # root = lxml.html.fromstring(s)
    # anchors = root.cssselect("a")
    # links = [a.get("href") for a in anchors]
    return

def test1():
    j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')

    html = urlopen("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20171026/FutureDataDaily.xls")
    data = html.read()
    print(data)
    return
def test2():
    session = requests.Session()
    # params = {'username': 'username', 'password': 'password'}
    s = session.post("http://www.czce.com.cn/portal/index.htm")

    print(s.cookies.get_dict())
    print("-----------")
    print("Going to profile page...")
    # s = session.get("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm")
    # http://www.czce.com.cn/portal/DFSStaticFiles/Future/2017/20171026/FutureDataDaily.xls
    # http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180522/FutureDataHolding.txt
    # http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180523/FutureDataHolding.htm
    # url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataTradeamt.htm'
    url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180523/FutureDataHolding.htm'
    s = session.get(url)
    s.encoding = 'gbk'
    print(s.text)
    # import pandas as pd
    # dfs = pd.read_html(s.text)
    # print(dfs)
    # i=0
    # for df in dfs:
    #     df.to_csv("zhenzhoutest{id}.csv".format(id=i), encoding='gbk')
    #     i += 1
    try:
        import lxml
        root = lxml.html.fromstring(s.text)
    except Exception as e:
        print(e)
        return
    for child in root:
        print("_" * 30)
        print(child.tag, child.attrib)
        for grandchild in child:
            print(grandchild.tag, grandchild.attrib)
    # dfs.to_csv("zhenzhoutest.csv")
    return

def main():
    test2()
    return
if __name__ == '__main__':
    main()
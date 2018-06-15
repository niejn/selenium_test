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

def czce_scrape(year=2018, month=6, day=11):
    from lxml import html
    url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/' \
          '{year:>04}/{year:>04}{month:>02}{day:>02}/FutureDataHolding.htm'.format(year=year, month=month, day=day)

    parser = html.HTMLParser(encoding='gbk')
    # root = html.document_fromstring(content, parser=parser)
    tree = html.parse(url, parser=parser)
    # tree.docinfo
    table = tree.findall('//table')[1]
    data = [
        [td.text_content().strip() for td in row.findall('td')]
        for row in table.findall('tr')
    ]

    df = pd.DataFrame(data, )

    df[0] = df[0].str.replace('\xa0', '')
    print(df)
    form_header = ['品种', '合约', '合计']
    temp_index = []
    start_index = []
    import collections
    header_index_dict = collections.OrderedDict()
    for a_header in form_header:
        a_index_list = df.index[df[0].str.contains(a_header)].tolist()
        if not a_index_list:
            continue
        header_index_dict.update({a_header: a_index_list})

    if '品种' in header_index_dict:
        contracts = header_index_dict['品种']
        if '合计' not in header_index_dict:
            print("Error")
        end_index = header_index_dict['合计']
        for beg, end in zip(contracts, end_index):
            t_df = df[beg:end]
            t_df.reset_index(inplace=True, drop=True)
            print(t_df)
            h_str = t_df.iat[0, 0]
            # '品种：苹果AP 日期：2018-05-23'
            import re
            # m = re.match(
            #     r"品种：(?P<productname>[\u4e00-\u9fa5]+)(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)", h_str)
            m = re.match(
                r"品种：(?P<productname>[\u4e00-\u9fa5]+)?(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)",
                h_str)
            t_instrumentid = m.group('instrumentid')
            t_productname = m.group('productname')
            if not t_productname:
                t_productname = "EMPTY"
            t_date = m.group('date')
            # productname 铜 instrumentid cu1804
            t_df = t_df.drop([0, 1])
            t_df['instrumentid'] = t_instrumentid
            t_df['productname'] = t_productname
            t_df['date'] = t_date
            print(t_df)
            col_names = ['rank', 'PARTICIPANTABBR1', 'CJ1', 'CJ1_CHG',
                         'PARTICIPANTABBR2', 'CJ2', 'CJ2_CHG',
                         'PARTICIPANTABBR3', 'CJ3', 'CJ3_CHG',
                         'instrumentid', 'productname', 'date']
            t_df.columns = col_names
            t_df['date'] = pd.to_datetime(t_df['date'])
            print(t_df)
            from db_insert2 import set_ranks_df
            t_df = t_df.drop(columns='date')
            set_ranks_df(t_df, year=year, month=month, day=day, exchange='CZCE')

    if '合约' in header_index_dict:
        instruments_index = header_index_dict['合约']
        len_instruments_index = len(instruments_index)
        if '合计' not in header_index_dict:
            print("Error")
        end_index = header_index_dict['合计']
        end_index = end_index[-len_instruments_index:]
        for beg, end in zip(instruments_index, end_index):
            t_df = df[beg:end]
            t_df.reset_index(inplace=True, drop=True)
            print(t_df)
            h_str = t_df.iat[0, 0]
            import re
            # m = re.match(
            #     r"品种：(?P<productname>[\u4e00-\u9fa5]+)(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)", h_str)
            m = re.match(
                r"合约：(?P<productname>[\u4e00-\u9fa5]+)?(?P<instrumentid>[a-zA-Z\d]+)\W*日期：(?P<date>[\d-]+)",
                h_str)
            t_instrumentid = m.group('instrumentid')
            t_productname = m.group('productname')
            if not t_productname:
                t_productname = "EMPTY"
            t_date = m.group('date')
            # productname 铜 instrumentid cu1804
            t_df = t_df.drop([0, 1])
            t_df['instrumentid'] = t_instrumentid
            t_df['productname'] = t_productname
            t_df['date'] = t_date
            print(t_df)
            col_names = ['rank', 'PARTICIPANTABBR1', 'CJ1', 'CJ1_CHG',
                         'PARTICIPANTABBR2', 'CJ2', 'CJ2_CHG',
                         'PARTICIPANTABBR3', 'CJ3', 'CJ3_CHG',
                         'instrumentid', 'productname', 'date']
            t_df.columns = col_names
            t_df['date'] = pd.to_datetime(t_df['date'])
            print(t_df)
            from db_insert2 import set_ranks_df
            t_df = t_df.drop(columns='date')
            set_ranks_df(t_df, year=year, month=month, day=day, exchange='CZCE')

    return

def html_parse(year=2018, month=6, day=11):
    from lxml import html
    url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/' \
          '{year:>04}/{year:>04}{month:>02}{day:>02}/FutureDataHolding.htm'.format(year=year, month=month, day=day)

    parser = html.HTMLParser(encoding='gbk')
    # root = html.document_fromstring(content, parser=parser)
    tree = html.parse(url, parser=parser)
    # tree.docinfo
    table = tree.findall('//table')[1]
    data = [
        [td.text_content().strip() for td in row.findall('td')]
        for row in table.findall('tr')
    ]

    df = pd.DataFrame(data, )


    df[0] = df[0].str.replace('\xa0', '')
    print(df)
    form_header = ['品种', '合约', '合计' ]
    temp_index = []
    start_index = []
    import collections
    header_index_dict = collections.OrderedDict()
    for a_header in form_header:
        a_index_list = df.index[df[0].str.contains(a_header)].tolist()
        if not a_index_list:
            continue
        header_index_dict.update({a_header: a_index_list})

    if '品种' in header_index_dict:
        contracts = header_index_dict['品种']
        if '合计' not in header_index_dict:
            print("Error")
        end_index = header_index_dict['合计']
        for beg, end in zip(contracts, end_index):
            t_df = df[beg:end]
            t_df.reset_index(inplace=True, drop=True)
            print(t_df)
            h_str = t_df.iat[0,0]
            # '品种：苹果AP 日期：2018-05-23'
            import re
            # m = re.match(
            #     r"品种：(?P<productname>[\u4e00-\u9fa5]+)(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)", h_str)
            m = re.match(
                r"品种：(?P<productname>[\u4e00-\u9fa5]+)?(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)",
                         h_str)
            t_instrumentid = m.group('instrumentid')
            t_productname = m.group('productname')
            if not t_productname:
                t_productname = "EMPTY"
            t_date = m.group('date')
            # productname 铜 instrumentid cu1804
            t_df = t_df.drop([0,1])
            t_df['instrumentid'] = t_instrumentid
            t_df['productname'] = t_productname
            t_df['date'] = t_date
            print(t_df)
            col_names = ['rank', 'PARTICIPANTABBR1', 'CJ1', 'CJ1_CHG',
                         'PARTICIPANTABBR2', 'CJ2', 'CJ2_CHG',
                         'PARTICIPANTABBR3', 'CJ3', 'CJ3_CHG',
                         'instrumentid', 'productname', 'date']
            t_df.columns = col_names
            t_df['date'] = pd.to_datetime(t_df['date'])
            print(t_df)
            from db_insert2 import set_ranks_df
            set_ranks_df(t_df, year=2018, month=5, day=23, exchange='CZCE')


    if '合约' in header_index_dict:
        instruments_index = header_index_dict['合约']
        len_instruments_index = len(instruments_index)
        if '合计' not in header_index_dict:
            print("Error")
        end_index = header_index_dict['合计']
        end_index = end_index[-len_instruments_index:]
        for beg, end in zip(instruments_index, end_index):
            t_df = df[beg:end]
            t_df.reset_index(inplace=True, drop=True)
            print(t_df)
            h_str = t_df.iat[0,0]
            import re
            # m = re.match(
            #     r"品种：(?P<productname>[\u4e00-\u9fa5]+)(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)", h_str)
            m = re.match(
                r"合约：(?P<productname>[\u4e00-\u9fa5]+)?(?P<instrumentid>[a-zA-Z\d]+)\W*日期：(?P<date>[\d-]+)",
                h_str)
            t_instrumentid = m.group('instrumentid')
            t_productname = m.group('productname')
            if not t_productname:
                t_productname = "EMPTY"
            t_date = m.group('date')
            # productname 铜 instrumentid cu1804
            t_df = t_df.drop([0, 1])
            t_df['instrumentid'] = t_instrumentid
            t_df['productname'] = t_productname
            t_df['date'] = t_date
            print(t_df)
            col_names = ['rank', 'PARTICIPANTABBR1', 'CJ1', 'CJ1_CHG',
                         'PARTICIPANTABBR2', 'CJ2', 'CJ2_CHG',
                         'PARTICIPANTABBR3', 'CJ3', 'CJ3_CHG',
                         'instrumentid', 'productname', 'date']
            t_df.columns = col_names
            t_df['date'] = pd.to_datetime(t_df['date'])
            print(t_df)
            from db_insert2 import set_ranks_df
            set_ranks_df(t_df, year=year, month=month, day=day, exchange='CZCE')


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
    import datetime
    today = datetime.datetime(2018, 6, 14)
    endday = datetime.datetime(2018, 6, 8)
    for i in range(30):
        from shfe_spider import getLastWeekDay
        weekday = getLastWeekDay(today)
        today = weekday
        if today <= endday:
            break
        print(weekday)
        czce_scrape(year=weekday.year, month=weekday.month, day=weekday.day)
        from time import sleep
        sleep(2)
    # czce_scrape()
    # html_parse()
    # test2()
    return
if __name__ == '__main__':
    main()
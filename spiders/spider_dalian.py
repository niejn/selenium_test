from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from io import StringIO, BytesIO
from lxml import html
from lxml import etree
import requests
import re
import pandas as pd

'''
POST /publicweb/quotesdata/memberDealPosiQuotes.html HTTP/1.1
Host: www.dce.com.cn
Connection: keep-alive
Content-Length: 136
Cache-Control: max-age=0
Origin: http://www.dce.com.cn
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: td_cookie=436593655; JSESSIONID=4DE9E9C32F9F4CA9C3958AA0A6A6B8CB; WMONID=m4g0pbcRS_Y; td_cookie=580194899
memberDealPosiQuotes.variety: b
memberDealPosiQuotes.trade_type: 0
year: 2018
month: 4
day: 14
contract.contract_id: all
contract.variety_id: b
'''
def trim_df():
    t_df = pd.read_csv('t_df_dalian.csv')
    a_index_list = t_df.index[t_df['rank'].str.contains('总计')].tolist()
    print(t_df)
    t_df.drop(t_df[t_df['rank'].str.contains('总计')].index, inplace=True, axis='index')
    t_df.drop(['rank2', 'rank3'], axis='columns', inplace=True)
    print(t_df)
    return


# month 为真实月份减少1
def get_dalian_ranks(year=2018, month=5, day=11):
    minus_month = int(month) - 1
    values = {
        'memberDealPosiQuotes.variety': 'b',
        'memberDealPosiQuotes.trade_type': '0',
        'year': str(year),
        'month': str(minus_month),
        'day': str(day),
        'contract.contract_id': 'all',
        'contract.variety_id': 'b',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Origin':'http://www.dce.com.cn',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'www.dce.com.cn',
        'Referer': 'http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',

    }
    url = "http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html"
    base_url = "http://www.dce.com.cn/publicweb/quotesdata/memberDealPosiQuotes.html"
    session = requests.Session()
    session.headers.update(headers)
    base_html = session.get(base_url)
    print(base_html.text)
    print(session.headers)
    session.headers.update(headers)
    print(session.headers)
    variety_list = ['a', 'b', 'm', 'y', 'p', 'c', 'cs', 'jd', 'fb', 'bb', 'l', 'v', 'pp', 'j', 'jm', 'i']
    cn_variety_names = ['豆一', '豆二', '豆粕', '豆油', '棕榈油', '玉米', '玉米淀粉', '鸡蛋', '纤维板',
                        '胶合板', '聚乙烯', '聚氯乙烯', '聚丙烯', '焦炭', '焦煤', '铁矿石',]

    # s = session.post(url, values)
    # print(s.text)
    # tree = html.fromstring(s.text)
    # table = tree.xpath('//*[@id="printData"]/div/table[2]')[0]
    # print(table)
    # data = [
    #     [td.text_content().strip() for td in row.findall('td')]
    #     for row in table.findall('tr')
    # ]
    # print(data)
    # df = pd.DataFrame(data, )
    df = None
    for a_var, cn_name in zip(variety_list, cn_variety_names):
        values['contract.variety_id'] = a_var
        s = session.post(url, values,)
        print(s.text)
        tree = html.fromstring(s.text)
        table = tree.xpath('//*[@id="printData"]/div/table[2]')[0]
        print(table)
        data = [
            [td.text_content().strip() for td in row.findall('td')]
            for row in table.findall('tr')
        ]
        print(data)
        col_names = ['rank', 'PARTICIPANTABBR1', 'CJ1', 'CJ1_CHG',
                     'rank2', 'PARTICIPANTABBR2', 'CJ2', 'CJ2_CHG',
                     'rank3', 'PARTICIPANTABBR3', 'CJ3', 'CJ3_CHG',
                     ]
        t_df = pd.DataFrame(data, columns=col_names)
        t_df.dropna(axis='index', inplace=True)
        # t_df.columns = col_names
        print(t_df)
        t_df.to_csv('t_df_dalian_{instrument}.csv'.format(instrument=a_var), index=False)
        # df[0].str.contains(a_header)
        t_df.drop(t_df[t_df['rank'].str.contains('总计')].index, inplace=True, axis='index')
        t_df.drop(['rank2', 'rank3'], axis='columns', inplace=True)
        print(t_df)
        t_df['instrumentid'] = a_var
        t_df['productname'] = cn_name
        import datetime
        today = datetime.datetime.now()
        t_df['date'] = today
        if df is None:
            df = t_df
        else:
            df = df.append(t_df)

    print(df)
    df.to_csv('t_df_dalian_sum.csv', index=False)
    from db_insert2 import set_ranks_df
    set_ranks_df(df, year=year, month=month, day=day, exchange='DCE')
    return


def main():
    # trim_df()
    get_dalian_ranks()
    return

if __name__ == '__main__':
    main()
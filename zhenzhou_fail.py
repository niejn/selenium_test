from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from urllib.request import urlopen
import json
import requests



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
    s = session.get("http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.txt")
    print(s.text)
    return

def main():
    test2()
    return
if __name__ == '__main__':
    main()
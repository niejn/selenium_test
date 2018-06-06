
from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json

'''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Connection:keep-alive
Cookie:td_cookie=978232345; BIGipServerwww_cbd=859613376.23067.0000; 
JSESSIONID=P6LChmJW5Bljnn1ty2nXvy2KMtvgQcDVGphP8pWjT2KfghhsJ8kJ!-1106748389; 
TS014ada8c=0169c5aa326c79ab9435ea5f82ce7bd3a48f37c042ae0caef379338ddbe1a50d283b833a82cc770ef42a41c3abb5de389ac9f6a59f
Host:www.czce.com.cn
Referer:http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
'''
def request_ajax_url(url,body=None,referer=None,cookie=None,**headers):
    req = Request(url)

    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
    req.add_header('Accept-Encoding','gzip, deflate')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
    req.add_header('Host', 'www.czce.com.cn')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36')

    if cookie:
        req.add_header('Cookie',cookie)

    if referer:
        req.add_header('Referer',referer)

    if headers:
        for k in headers.keys():
            req.add_header(k,headers[k])

    # postBody = json.dumps(body)
    # data = urlencode(postBody).encode(encoding='UTF8')
    response = urlopen(req, )
    re_data = response.read()
    re_data = re_data.decode('utf8')

    print(re_data)
    if response:

        return response

def test():
    '''
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Cache-Control: max-age=0
    Connection: keep-alive
    Cookie: td_cookie=4076000372; BIGipServerwww_cbd=842836160.23067.0000; JSESSIONID=SLq1hVTJlrv4QWBgxYPRN2G18GXH35TGqZYtSVSmdcJF9f6bNfTS!712259343; TS014ada8c=0169c5aa32d0ddd752d8b801f3963f99c9ffe2f89a3cc7350c7a8057eac687f25da48d67ef7c38a277f42a68448c826487cff39e55
    Host: www.czce.com.cn
    If-Modified-Since: Mon, 16 Apr 2018 07:38:39 GMT
    Referer: http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataTradeamt.htm
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    :return:
    '''
    values = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'td_cookie=978232345; BIGipServerwww_cbd=859613376.23067.0000; '
                  'JSESSIONID=P6LChmJW5Bljnn1ty2nXvy2KMtvgQcDVGphP8pWjT2KfghhsJ8kJ!-1106748389;'
                  'TS014ada8c=0169c5aa326c79ab9435ea5f82ce7bd3a48f37c042ae0caef379338ddbe1a50d283b833a82cc770ef42a41c3abb5de389ac9f6a59f',
        'Host': 'www.czce.com.cn',
        'Referer': 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        # '': '',
    }

    # data = urlencode(values)
    # url = "http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataHolding.htm"
    url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180416/FutureDataTradeamt.htm'
    data = urlencode(values).encode(encoding='UTF8')
    request = Request(url, data)

    response = urlopen(request, timeout=4)
    re_data = response.read()
    re_data = re_data.decode('utf8')

    print(re_data)
    return
def main():
    test()
#     login_body = {"action": "login", "UserName": "xfkxfk", "Password": "123456", "AutomaticLogin": False}
#     '''td_cookie=978232345; BIGipServerwww_cbd=859613376.23067.0000;
# JSESSIONID=P6LChmJW5Bljnn1ty2nXvy2KMtvgQcDVGphP8pWjT2KfghhsJ8kJ!-1106748389;
# TS014ada8c=0169c5aa326c79ab9435ea5f82ce7bd3a48f37c042ae0caef379338ddbe1a50d283b833a82cc770ef42a41c3abb5de389ac9f6a59f'''
#     cookies = {'td_cookie':'978232345', 'BIGipServerwww_cbd':'859613376.23067.0000',
#                'JSESSIONID':'P6LChmJW5Bljnn1ty2nXvy2KMtvgQcDVGphP8pWjT2KfghhsJ8kJ!-1106748389',
#                'TS014ada8c':'0169c5aa326c79ab9435ea5f82ce7bd3a48f37c042ae0caef379338ddbe1a50d283b833a82cc770ef42a41c3abb5de389ac9f6a59f', }
#     url = 'http://www.czce.com.cn/portal/DFSStaticFiles/Future/2018/20180309/FutureDataHolding.htm'
#     request_ajax_url(url=url, cookie=cookies)
    return

if __name__ == '__main__':
    main()
# http://www.cffex.com.cn/sj/ccpm/201803/09/IF.xml
'''

Request URL:http://www.cffex.com.cn/sj/ccpm/201803/09/IF.xml
Request Method:GET
Status Code:200 OK (from disk cache)
Remote Address:116.228.92.1:80
Referrer Policy:no-referrer-when-downgrade
'''

from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json
from urllib.request import urlopen
import json
# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')
# http://www.cffex.com.cn/sj/ccpm/201804/09/IF.xml
html = urlopen("http://www.cffex.com.cn/sj/ccpm/201804/09/IF.xml")
data = html.read()
print(data)
str_data = bytes.decode(data)
j = json.loads(str_data)
print(j)
print(html.read())
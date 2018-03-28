from urllib.request import urlopen
import json
# j = json.loads('{"one" : "1", "two" : "2", "three" : "3"}')

html = urlopen("http://www.shfe.com.cn/data/dailydata/kx/pm20180307.dat")
data = html.read()
str_data = bytes.decode(data)
j = json.loads(str_data)
print(html.read())



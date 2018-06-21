import re
t_str = "javascript:setVariety('a');"
m = re.match(r"javascript:setVariety\(\'(?P<instrumentid>[a-z]+)\'\);", t_str)
t_instrumentid = m.group('instrumentid')
print(t_instrumentid)
m = re.match(r"javascript:setVariety(?P<instrumentid>[()a-z']+);", t_str)
t_instrumentid = m.group('instrumentid')
print(t_instrumentid)



h_str = '品种：PTA\n日期：2018-05-23'
# h_str = '品种：苹果AP \n 日期：2018-05-23'
# m = re.match(r"品种：(?P<productname>[\u4e00-\u9fa5]+)(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)", h_str)
m = re.match(r"品种：(?P<productname>[\u4e00-\u9fa5]+)?(?P<instrumentid>[a-zA-Z]+)\W*日期：(?P<date>[\d-]+)", h_str)
t_instrumentid = m.group('instrumentid')
temp = m.groupdict()
if 'productname' in temp:
    t_productname = m.group('productname')
else:
    t_productname = "EMPTY"
t_date = m.group('date')

# '品种：苹果AP 日期：2018-05-23'
m = re.match(r"品种：(?P<contract>\w+)\W*日期：(?P<date>[\d-]+)", '品种：苹果AP \n 日期：2018-05-23')
print(m.group('contract'))
print(m.group('date'))

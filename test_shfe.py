# http://www.shfe.com.cn/statements/dataview.html?paramid=pm

# driver.execute_script(js)

from time import sleep

from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
# http://www.shfe.com.cn/data/dailydata/kx/pm20180301.dat
driver.get("http://www.shfe.com.cn/data/dailydata/kx/pm20180301.dat")
# driver.get
# driver.get("http://www.shfe.com.cn/statements/dataview.html?paramid=pm")
# get the search textbox
# /html/body/header/div[2]/div[2]/div[1]/section/ul/li[1]/a
# MY ACCOUNT
# account_link = driver.find_element_by_link_text("MY ACCOUNT")
'''<td class=" ui-datepicker-week-end no-data" 
onclick="DP_jQuery_1520581711786.datepicker._selectDay('#calendar',2,2018, this);
return false;"><a class="ui-state-default" href="#">4</a></td>'''
# js = 'DP_jQuery_1520581711786.datepicker._selectDay(1,2,2018, this)'
# driver.execute_script(js)
# button = driver.find_element_by_xpath("/html/body/header/div[2]/div[2]/div[1]/section/ul/li[1]/a")
# button.click()
# //*[@id="dateinput"]
# executeScript("var setDate=document.getElementById(\"train_date\");setDate.removeAttribute('readonly');") ;
js = 'var setDate=document.getElementById(\"dateinput\");setDate.removeAttribute(\'readonly\');'
driver.execute_script(js)
# close the browser window
# setDatElement = driver.find_element_by_xpath('//*[@id="dateinput"]')
# setDatElement.clear();
# setDatElement.sendKeys("2018-03-01");
# //*[@id="li_all"]/a/span
# //*[@id="li_all"]/a/span
# //*[@id="calendar"]/div/table/tbody
button = driver.find_element_by_xpath("//*[@id=\"li_all\"]")
button.click()
print("finished")
sleep(10000)
driver.quit()

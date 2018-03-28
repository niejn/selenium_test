from selenium import webdriver
options = webdriver.FirefoxOptions()
options.set_headless()
# options.add_argument(‘-headless‘)
# options.add_argument('--disable-gpu')
driver=webdriver.Firefox(firefox_options=options)
driver.get('http://httpbin.org/user-agent')
driver.get_screenshot_as_file('test.png')
driver.close()
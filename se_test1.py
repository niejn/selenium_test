from time import sleep

from selenium import webdriver

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("http://demo.magentocommerce.com/")
# get the search textbox
# /html/body/header/div[2]/div[2]/div[1]/section/ul/li[1]/a
# MY ACCOUNT
account_link = driver.find_element_by_link_text("MY ACCOUNT")
button = driver.find_element_by_xpath("/html/body/header/div[2]/div[2]/div[1]/section/ul/li[1]/a")
button.click()
# //*[@id="edit-keys"]
search_field = driver.find_element_by_xpath("//*[@id=\"edit-keys\"]")
search_field.clear()
# # enter search keyword and submit
search_field.send_keys("phones")
# search_field.submit()
# //*[@id="page-search-btn"]
search_button = driver.find_element_by_xpath("//*[@id=\"page-search-btn\"]")
search_button.click()
# # get all the anchor elements which have product names displayed
# # #currently on result page using find_elements_by_xpath method
# /html/body/div[3]/div/div[2]/div/div[2]/ul
# gss-result
products = driver.find_elements_by_xpath("//li[@class='gss-result']")
# # get the number of anchor elements found
print("Found " + str(len(products)) + " products:")
# # iterate through each anchor element and print the text that is#name of the product
for product in products:
    print(product.text)
a_pro = products[0]
# class="result-title"
test = a_pro.find_element_by_xpath("//div[@class='result-title']")
print(test.text)
# product(a_pro.text)
# a_pro.li
# //*[@id="gl-container"]/div[2]/div/div[2]/ul/li[1]/div[1]

# close the browser window
print("finished")
sleep(10000)
driver.quit()

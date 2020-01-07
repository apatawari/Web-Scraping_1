from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\chromedriver\chromedriver.exe", chrome_options=option)
browser.get("https://pandamonic.poetry.blog/")

# find_elements_by_xpath returns an array of selenium objects.
pin_element_1 = browser.find_elements_by_xpath('//div[@class="entry-content"]/p[@class="has-text-align-center"]/a[@*]')
pin_element_2 = browser.find_elements_by_xpath('//div[@class="entry-content"]/p[@class="has-text-align-center"]/em/a[@*]')



# use list comprehension to get the actual repo titles and not the selenium objects.
links_1 = [x.get_attribute("href") for x in pin_element_1]
links_2 = [x.get_attribute("href") for x in pin_element_2]

# print out all the titles.
print('links:')
#print(links_1, '\n') 
#print(links_2,'\n')
links = links_1 + links_2
print(links)
print(len(links))
#print(len(links_1) + len(links_2))


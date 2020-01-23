from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from bs4 import BeautifulSoup
import requests


option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\chromedriver\chromedriver.exe", chrome_options=option)
browser.get("https://aminoapps.com/c/poetry/recent/")

#pin_element_1 = browser.find_elements_by_xpath('//section[@class="main-postlist content"]/section[@class="post-list new-post-list "]/div[@*]/a[@*]')

#######pin_element_1 = browser.find_elements_by_xpath('//section[@class="global-body"]//a[@*]')
#pin_element_1 = browser.find_elements_by_xpath("//section[@class='post-list new-post-list']//div[@class='list-item mutual-block']//article[@class='post post-blog']//a[@*]")
pin_element_1 = browser.find_elements_by_xpath("//section[@class='post-list new-post-list']//a[@*]")
#pin_element_1 = browser.find_elements_by_xpath('//a[@*]')
links_1 = [x.get_attribute("href") for x in pin_element_1]

print(links_1)
print(len(links_1))
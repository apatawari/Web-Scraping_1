#importing the libraries 

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from bs4 import BeautifulSoup
import requests
import time

# setting up the driver and web browser 

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\chromedriver\chromedriver.exe", chrome_options=option)
browser.get("https://aminoapps.com/c/poetry/recent/")

# Setting up the scrolling mechanism 


SCROLL_PAUSE_TIME = 6

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
for i in range(2):
    pin_element_1 = browser.find_elements_by_xpath('//section[@class="global-body"]//section[@class="community-content"]//section[@class="main-postlist content"]//section[@class="post-list new-post-list "]/div[@*]/article[1]/a[1]')

    links_1 = [x.get_attribute("href") for x in pin_element_1]
    while True:
    # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# clearing repeating links 

links = [] 
for temp in links_1: 
    if temp not in links: 
            links.append(temp) 

print(links)
print(len(links))

# To Use BeautifulSoup to extract the data from the URLs 
counter = 0

for url in links:

    unsafe = '"<>#%{}|\^~[]`'  # Weeding out the unsafe characters from the URLs
    for char in unsafe:
        url = url.replace(char,"")

# Accessing the page using BeautifulSoup
    response = requests.get(url,timeout=5)
    content = BeautifulSoup(response.content, "html5lib")

# Getting the specific data from the webpage 
    title = content.find('h1',attrs = {"class":"title community-color force-word-break"}).text
    poetry = content.find('div', attrs={"class": "post-content-toggle"}).text
    counter += 1

# Printing the data we extracted
    print("article number:",counter)
    print(title)
    print('\n')
    print(poetry,'\n')
    
 #Writing them into text files 
    with open('article_'+ str(counter)+'.txt', "w", encoding="utf-8") as f:
        f.write(title + "\n")
        f.write(poetry)




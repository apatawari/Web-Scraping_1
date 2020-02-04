#importing the libraries 

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

def the_type(x):
    """ To find the class name of the type of content """
    a = type(x)
    b = str(a.__name__)
    return(b)

# setting up the driver and web browser 

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\chromedriver\chromedriver.exe", chrome_options=option)
browser.get("https://aminoapps.com/c/poetry/recent/")

# Setting up the scrolling mechanism 
elm = browser.find_element_by_tag_name('html')
target_links = 100
no_of_links = 0
while no_of_links < target_links:
    elm.send_keys(Keys.END)
    time.sleep(5)
    pin_element_1 = browser.find_elements_by_xpath('//section[@class="global-body"]//section[@class="community-content"]//section[@class="main-postlist content"]//section[@class="post-list new-post-list "]/div[@*]/article[1]/a[1]')
    links_1 = [x.get_attribute("href") for x in pin_element_1]

# clearing repeating links 

    links = [] 
    for temp in links_1: 
        if temp not in links: 
                links.append(temp) 
    no_of_links = len(links)

print(links)
print(len(links))

# To Use BeautifulSoup to extract the data from the URLs 
counter = 0

for url in links:

    unsafe = '"<>#%{}|\^~[]`'  # Weeding out the unsafe characters from the URLs
    for char in unsafe:
        url = url.replace(char,"") 

# Accessing the page using BeautifulSoup
    response = requests.get(url,timeout=10)
    content = BeautifulSoup(response.content, "html5lib")

# Getting the specific data from the webpage 
    title = content.find('h1',attrs = {"class":"title community-color force-word-break"})
    title_type = the_type(title)

    if title_type == 'NoneType':
        continue
    else:
        title = title.text

    poetry = content.find('div', attrs={"class": "post-content-toggle"})
    poetry_type = the_type(poetry)

    if poetry_type == 'NoneType':
        continue
    else:
        poetry = poetry.text
    counter += 1

# Printing the data we extracted
    print("article number:",counter)
    print(title,'\n')
    print(poetry,'\n')
    
 #Writing them into text files 
    """with open('article_'+ str(counter)+'.txt', "w", encoding="utf-8") as f:
        f.write(title + "\n")
        f.write(poetry)"""




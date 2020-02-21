#importing the libraries 

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import os

links = []
counter = 0

def the_type(x):
    """ To find the the type of content and return the name"""
    a = type(x)
    b = str(a.__name__)
    return(b)

def scrolling_mech():
    """To scroll and obtain the links of the articles"""

    target_links = 100
    no_of_links = 0
    global links

    while no_of_links < target_links:
        elm.send_keys(Keys.END)
        time.sleep(5)
        pin_element_1 = browser.find_elements_by_xpath('//section[@class="global-body"]//section[@class="community-content"]//section[@class="main-postlist content"]//section[@class="post-list new-post-list "]/div[@*]/article[1]/a[1]')
        links_1 = [x.get_attribute("href") for x in pin_element_1]

# clearing repeating links 
        for temp in links_1: 
            if temp not in links: 
                    links.append(temp) 
        no_of_links = len(links)

    links = links[:target_links]
    print(links)
    print(len(links))
    extraction(links)

def extraction(links):
    """To extract the text from the articles"""

    global counter
    for url in links:
        poetry = ''
        unsafe = '"<>#%{}|\^~[]`'  # Weeding out the unsafe characters from the URLs
        for char in unsafe:
            url = url.replace(char,"") 
# Accessing the page using BeautifulSoup
        try:
            response = requests.get(url,timeout=10)
        except requests.exceptions.Timeout:
            response = requests.get(url,timeout=10)
      
        content = BeautifulSoup(response.content, "html5lib")
# Getting the specific data from the webpage 
        title = content.find('h1',attrs = {"class":"title community-color force-word-break"})
        title_type = the_type(title)

        if title_type == 'NoneType':
            continue
        else:
            title = title.text

        poetry_html = content.find('div', attrs={"class": "post-content-toggle"})
        poetry_type = the_type(poetry_html)

        if poetry_type == 'NoneType':
            continue
        else:
            for i in poetry_html:
                try:
                    x = i.text
                    poetry = poetry + '\n' + x
                except AttributeError:
                    continue
        counter += 1
        # Printing the data we extracted
        print("article number:",counter)
        print(title,'\n')
        print(poetry,'\n')
        time.sleep(2)
        save_article(poetry,counter)
    
def save_article(poetry,counter):
    """To save the articles in the specified path"""

    filepath = os.path.join(saved_path,'article_' + str(counter) + '.txt')
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    f = open(filepath,'w',encoding='UTF-8')
    f.write(poetry)
    return
    
# setting up the driver and web browser 

option = webdriver.ChromeOptions()
option.add_argument(" — incognito")

browser = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\chromedriver\chromedriver.exe", chrome_options=option)
browser.get("https://aminoapps.com/c/poetry/recent/")
saved_path = input("Enter the path of the folder where the articles are to be saved")

# Setting up the scrolling mechanism 
elm = browser.find_element_by_tag_name('html')
scrolling_mech()

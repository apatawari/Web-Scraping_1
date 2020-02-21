#Importing the libraries 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import os

#chrome arguments 
option = webdriver.ChromeOptions()
option.add_argument(" — incognito")
option.add_argument('--ignore-certificate-errors')
option.add_argument('--ignore-ssl-errors')


counter = 0

def extracting_links(i):
    """To extract the links from the webpage"""
    
    global links
    page = browser.find_element_by_link_text(i)
    browser.implicitly_wait(5)
    page.click()
    browser.implicitly_wait(5)

    pin_element_1 = browser.find_elements_by_xpath('//div[@id="c_articlelist_stories_1"]//ul[@id="content"]//li//a[@*]')
    pin_element_2 = browser.find_elements_by_xpath('//div[@id="c_articlelist_stories_2"]/ul[1]//li//a[@*]')
    links_1 = [x.get_attribute("href") for x in pin_element_1]
    links_2 = [x.get_attribute("href") for x in pin_element_2]

    links_total = links_1 + links_2 
    
    for i in links_total:
        if i not in links:
            links.append(i)
    print(links)
    print(len(links))
    print(browser.current_url)
    return links


def extract_content(links):
    """To extract the article from the page"""

    for url in links:

        global counter
        counter+=1
        response = requests.get(url,timeout=5)
        content = BeautifulSoup(response.content, "html5lib")
        article = ''

        article_html = content.find('div', attrs={"class": "_3WlLe clearfix"})

        for i in article_html:
            try:
                x = i.text
                article = article + '\n' + x
            except AttributeError:
                y = str(i)
                article = article + '\n' + y

        print('article no:',counter)
        print('\n',article)

        save_article(article,counter)

def save_article(article,counter):
    """To save the articles in the specified path"""

    filepath = os.path.join(saved_path,'article_' + str(counter) + '.txt')
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    f = open(filepath,'w')
    f.write(article)


# To set up the browser, obtain the URL,Number of pages to extract from and, path to save the articles in:
browser = webdriver.Chrome(executable_path=r"C:\Users\admin\Desktop\chromedriver\chromedriver.exe", chrome_options=option)
premise = input("Url of the ToI page with a list of articles on a certain topic")
saved_path = input("Enter the path where the articles are to be stored")
pages = int(input("Enter the number of pages to extract"))
#  C:/Users/admin/Desktop/temp_p
# https://timesofindia.indiatimes.com/business/india-business/sensex
browser.get(premise)

links = []
pages = pages + 1
for i in range(1,pages):
    i = str(i)
    extracting_links(i)
extract_content(links)

    
#Importing the libraries 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time
import os
from html.parser import HTMLParser
from bs4.element import Comment

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)



def extract_content(link):
    """To extract the article from the page"""

    html = (requests.get(link,timeout=20)).content
    print(text_from_html(html))
def save_article(article,counter):
    """To save the articles in the specified path"""

    filepath = os.path.join(saved_path,'article_' + str(counter) + '.txt')
    if not os.path.exists(saved_path):
        os.makedirs(saved_path)
    f = open(filepath,'w')
    f.write(article)


link = input()
extract_content(link)
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path= r"C:/Users/admin/Desktop/chromedriver", options=options)

import time

driver.get("https://www.tripadvisor.com/Airline_Review-d8729157-Reviews-Spirit-Airlines#REVIEWS")
more_buttons = driver.find_elements_by_class_name("moreLink")
for x in range(len(more_buttons)):
  if more_buttons[x].is_displayed():
      driver.execute_script("arguments[0].click();", more_buttons[x])
      time.sleep(1)
page_source = driver.page_source

from bs4 import BeautifulSoup

soup = BeautifulSoup(page_source, 'lxml')
reviews = []
reviews_selector = soup.find_all('div', class_='reviewSelector')
for review_selector in reviews_selector:
    review_div = review_selector.find('div', class_='dyn_full_review')
    if review_div is None:
        review_div = review_selector.find('div', class_='basic_review')
    review = review_div.find('div', class_='entry').find('p').get_text()
    review = review.strip()
    reviews.append(review)

    
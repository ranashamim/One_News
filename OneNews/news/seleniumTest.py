import threading
import requests
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException as noElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json 

browser = webdriver.Chrome('/home/hooshmand/Documents/Git/Django/OneNews/One_News/OneNews/chromedriver')

browser.get('https://www.zoomit.ir/')
#element = browser.find_element_by_class_name("sc-73a1c33f-0 sc-77902f6f-4 bwgasb jRkftW")
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "jRkftW"))
    )
    articles_url_list = [element.get_attribute('href')
                    for element in WebDriverWait(browser, 5).until(
                        EC.visibility_of_all_elements_located((By.CLASS_NAME, "eUyGrf"))
                        )] 
finally:
    browser.quit()



def click_and_go_to_article_page(element):
    article_content = ""
    try:
        
        driver = webdriver.Chrome('/home/hooshmand/Documents/Git/Django/OneNews/One_News/OneNews/chromedriver')
        driver.get(element)

        # article 
        try:

            article_title = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
                        (By.TAG_NAME, 'h1'))).get_attribute('innerHTML')

        except TimeoutException:
            pass

        # article content
        try:

            articles_content_list = [element.text
                    for element in WebDriverWait(driver, 5).until(
                        EC.visibility_of_all_elements_located((By.CLASS_NAME, "brkdqE"))
                        )]
            
            for i in articles_content_list:
                article_content = article_content + i 


        except TimeoutException:
            pass

        article_source = str(element)
         

        article_dic = {'title': article_title, 'news_text': article_content, 'source': article_source}
        
        with open("Zoomit.json", "w", encoding='utf8') as json_file:
            json.dump( article_dic, json_file, ensure_ascii=False)
                

    except TimeoutException:
            pass



""" counter = 0
for article in articles_url_list:
    counter += 1
    threading.Thread(target=click_and_go_to_article_page, args=(article,)).start()
    time.sleep(4)
    if counter%2 == 0:
        time.sleep(60)
 """
threading.Thread(target=click_and_go_to_article_page, args=(articles_url_list[0],)).start()
time.sleep(4)
    
print('########################')

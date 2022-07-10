from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('D:/Ojjas/Ojjas-Whjr/Project-127/chromedriver')
browser.ger(START_URL)
time.sleep(10)

def scrape():
    header = ['name', 'distance', 'mass', 'radius']
    empty_list = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        for tr_tag in soup.find_all('tr', attrs = {'class', 'brightest_stars'}):
            th_tag = tr_tag.find_all('th')
            temp_list = []
            for index, th_tag in enumerate(th_tag):
                if index == 0:
                    temp_list.append(th_tag.find_all('a')[0].contents[0])
                else:
                    try:
                        temp_list.append(th_tag.contents[0])
                    except:
                        temp_list.append('')
            empty_list.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scrapper_2.csv', 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(empty_list)

scrape()
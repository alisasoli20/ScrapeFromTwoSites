import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import re
from selenium.common.exceptions import NoSuchElementException
from urllib import request



options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
element = ''
driver = webdriver.Chrome('C:\Python\chromedriver.exe',options=options)
driver.get('https://www.fragrancex.com')
element = driver.find_element_by_xpath('//*[@id="header"]/nav/div[1]/div[3]/div/div/ul[1]/li[2]/a')
element.click()
time.sleep(2)
#element = driver.find_element_by_xpath('//*[@id="subcat_1"]')
#element.click()
#time.sleep(2)
element = driver.find_element_by_xpath('//*[@id="SearchBlockAsyncForm"]/div/div/div/div/div/div/div[1]/div[1]')
text = element.text
text = text.split()
results = text[4]
print(results)
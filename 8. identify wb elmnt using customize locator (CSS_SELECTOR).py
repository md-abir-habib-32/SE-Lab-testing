from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)
driver.get('https://www.facebook.com/')
TAG & ID
driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc')
#Here tag is input and id is email [between these two have to use #]
TAG & CLASS
driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('abc')
#Here, tag is input and class is inputtext [between these two have to
use . ] {if the class name is larger, then consider only the first portion
upto any space or _}
TAG & Attributes
driver.find_element(By.CSS_SELECTOR,'input[data-testid="royal_email"]')
.send_keys('abcdef')
# Here, tag is input and as attribute used data-testid {between these
two have to use [ ], and inside [ ] have to keep attributes value}
TAG & CLASS & Attributes
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name=email]').se
nd_keys('xyz')
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name=pass]').sen
d_keys('123')
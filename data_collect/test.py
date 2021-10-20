# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 07:57:39 2021

@author: tango
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd
import itertools


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://baan.kaidee.com/c15-realestate-home')
time.sleep(10)
title_l = []
price_l = []
address_l = []
bed_l = []
bath_l = []
area_l = []

for num in range(0,4):
    print('next page')
    titles = driver.find_elements_by_class_name('_7f17f34f')
    prices = driver.find_elements_by_class_name('f343d9ce')
    addresses = driver.find_elements_by_class_name('_7afabd84')
    beds = driver.find_elements_by_css_selector("[aria-label='Beds']")
    baths = driver.find_elements_by_css_selector("[aria-label='Baths']")
    areas = driver.find_elements_by_css_selector("[aria-label='Area']")
       
    for i in range(len(titles)):
        title_l.append({'title' :titles[i].text})
        
    for i in range(len(prices)):
        price_l.append({'price' :prices[i].text})
    
    for i in range(len(addresses)):
        address_l.append({'address' :addresses[i].text})
        
    for i in range(len(beds)):
        bed_l.append({'bed' :beds[i].text})
    
    for i in range(len(baths)):
        bath_l.append({'bath' :baths[i].text})
        
    for i in range(len(areas)):
        area_l.append({'area' :areas[i].text})
                
    next_button = driver.find_element_by_css_selector("[title='ต่อไป']")
    next_button.click()
    time.sleep(1)

driver.close()

ab = itertools.chain(title_l, price_l, address_l, bed_l, bath_l, area_l)
ab = list(ab)
df = pd.DataFrame(ab)
df1 = df.apply(lambda x: pd.Series(x.dropna().values))
#df.to_csv('housing_data_thailand_2021.csv')

        
        



# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:23:01 2021

@author: tango
"""
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# get a list of link for each pages
def get_house_links(url, driver, pages=3):
    house_links=[]
    driver.get(url)
    time.sleep(10)
    for i in range(pages):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        listings = soup.find_all("a", class_="_287661cb")
        page_data = ['https://baan.kaidee.com'+row['href'] for row in listings]
        house_links.append(page_data)
        time.sleep(np.random.lognormal(0,1))
        next_button = soup.find_all("a", class_="b7880daf")
        next_button_link = ['https://baan.kaidee.com'+row['href'] for row in next_button]
        if i<pages-1:
            driver.get(next_button_link[-1])
    
    return house_links

# get html data for a specified url
def get_html_data(url, driver):
    driver.get(url)
    time.sleep(np.random.lognormal(0,1))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

# get price
def get_price(soup):
    try:
        price = soup.find(class_ = '_105b8a67').text
        return price
    except:
        return np.nan

# get address
def get_address(soup):
    try:
        address = soup.find(class_ = '_1f0f1758').text
        return address
    except:
        return np.nan

# get bedroom
def get_bed(soup):
    try:
        beds = soup.find_all(class_='fc2d1086')
        bed = beds[0].text
        bed = bed.replace(" ห้องนอน", "").lower()
        return int(bed)
    except:
        return np.nan
    
# get bathroom
def get_bath(soup):
    try:
        baths = soup.find_all(class_='fc2d1086')
        bath = baths[1].text
        bath = bath.replace(" ห้องน้ำ", "").lower()
        return int(bath)
    except:
        return np.nan
    
# get area
def get_area(soup):
    try:
        areas = soup.find_all(class_='fc2d1086')
        area = areas[2].text
        area = area.replace(" ตร.ว.", "").lower()
        return int(area)
    except:
        return np.nan
    
#get title
def get_title(soup):
    try:
        title = soup.find(class_='fcca24e0 fontCompensation').text
        return title
    except:
        return np.nan
    
#get description
def get_description(soup):
    try:
        description = soup.find(class_='_2015cd68 d320ecf0').text
        return description
    except:
        return np.nan

# get status
def get_status(soup):
    try:
        statuses = soup.find_all(class_='_812aa185')
        status = statuses[3].text
        return status
    except:
        return np.nan

# get listing date
def get_date(soup):
    try:
        dates = soup.find_all(class_='_812aa185')
        date = dates[4].text
        return date
    except:
        return np.nan
    
# flatten the list
def flatten_list(house_links):
    house_links_flat=[]
    for sublist in house_links:
        for item in sublist:
            house_links_flat.append(item)
    return house_links_flat

# go through the list and get the info you need
def get_house_data(driver,house_links_flat):
    house_data = []
    for link in house_links_flat:
        soup = get_html_data(link,driver)
        address = get_address(soup)
        areas = get_area(soup)
        beds = get_bed(soup)
        baths = get_bath(soup)
        descriptions = get_description(soup)
        listing_date = get_date(soup)
        prices = get_price(soup)
        status = get_status(soup)
        titles = get_title(soup)
        house_data.append([address,areas,beds,baths,descriptions,listing_date,prices,status,titles])
    return house_data

house_links_100pages = get_house_links('https://baan.kaidee.com/c15-realestate-home',driver,pages=100)
house_links_flat = flatten_list(house_links_100pages)
house_data_100pages = get_house_data(driver,house_links_flat)

columns = ['address','areas','beds','baths','descriptions','listing_date','prices','status','titles']
pd.DataFrame(house_data_100pages, columns = columns).to_csv('housing_data_thailand_2021.csv', index = False, encoding = "UTF-8")
        




            
        
        

                






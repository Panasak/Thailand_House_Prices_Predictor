# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:23:01 2021

@author: tango
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time
import pandas as pd

def get_listings(num_listings, verbose):

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.ddproperty.com/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8%E0%B8%82%E0%B8%B2%E0%B8%A2?market=residential')
    listings = []
    
    while len(listings) < num_listings:
        
        #Going through each offers in this page
        offer_buttons = driver.find_elements_by_class_name("nav-link")  # These are the buttons we're going to click.
        for offer_button in offer_buttons:  

            print("Progress: {}".format("" + str(len(listings)) + "/" + str(num_listings)))
            if len(listings) >= num_listings:
                break

            offer_button.click()  #You might 
            time.sleep(1)

            try:
                title = driver.find_element_by_class_name('h2 text-transform-none').text
            except NoSuchElementException:
                title = -1 #You need to set a "not found value. It's important."
            
            try:
                listing_type = driver.find_element_by_class_name('listing-property-type').text
            except NoSuchElementException:
                title = -1
                
            try:
                price = driver.find_element_by_class_name('element-label price').text
            except NoSuchElementException:
                title = -1
                
            try:
                number_of_bedroom = driver.find_element_by_class_name('property-info-element beds').text
            except NoSuchElementException:
                title = -1
                
            try:
                number_of_bathroom = driver.find_element_by_class_name('property-info-element baths').text
            except NoSuchElementException:
                title = -1

            #Printing for debugging
            if verbose:
                print("Title: {}".format(title))
                print("Listing Type: {}".format(listing_type))
                print("Price: {}".format(price))
                print("Number of bedroom: {}".format(number_of_bedroom))
                print("Number of bathroom: {}".format(number_of_bathroom))
                
            #TEST
            listings.append({"Title" : title,
            "Listing Type" : listing_type,
            "Price" : price,
            "Number of bedroom" : number_of_bedroom,
            "Number of bathroom" : number_of_bathroom})
        
        return listings

get_listings(2, True)
            
        
        

                






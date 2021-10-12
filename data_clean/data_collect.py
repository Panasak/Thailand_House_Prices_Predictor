# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 07:23:01 2021

@author: tango
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.ddproperty.com/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B2%E0%B8%A8%E0%B8%82%E0%B8%B2%E0%B8%A2?market=residential')
print(driver.title)
driver.quit()
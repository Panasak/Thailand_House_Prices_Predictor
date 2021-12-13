# Thailand House Prices Predictor: Project Overview
This project uses multiple linear regression to predict the house prices in Thailand
* Create a tool that estamates house prices in Thailand to help home buyers negotiate the prices when they are buying a house
* Scraped 2400 houses from baan.kaidee.com using python and selenium
* Engineered features from text of each house description to quantify the value the sellers put on views, schools, universities, and housing assosication
* Optimized Linear, Lasso, and Random Forest Regression using GridsearchCV to reach the best model
* Built a client facing API using flask
## Code and Resources Used
* **Python Version:** 3.7
* **Packages:** pandas, numpy, matplotlib, seaborn, selenium, flask, json, pickle
* **For Web Framework Requirements:** `pip install -r requirements.txt`
* **Scaper Article:** https://medium.com/@ben.sturm/scraping-house-listing-data-using-selenium-and-beautiful-soup-1cbb94ba9492
* **Flask Productization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2
## Web Scraping
Tweaked the web scraper from the article above to scrape 2400 house postings from baan.kaidee.com. With each job, we got the following:
*



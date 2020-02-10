# Dependencies
import os
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import numpy as np
import re
import datetime
from datetime import timedelta
import time
from selenium import webdriver

def scrape_info():
    driver = webdriver.Chrome()
    url = 'https://twitter.com/realDonaldTrump'

    driver.get(url)

    tweets = []
    tweetdate = []

    for j in range(5):
        tweet = driver.find_elements_by_xpath("//article/div/div[2]/div[2]/div[2]/span[1]")
        datetime_tweet = driver.find_elements_by_xpath("//article/div/div[2]/div[2]/div[2]/span/../../div/div/div/a")
        # print(len(tweet))
        # print(len(datetime_tweet))
        
        
        for i in range(len(tweet)):
            # print(tweet[i].text)
            # print(datetime_tweet[i].get_attribute('title'))
            # print('---------------------------------------------------------------------------')
            
            
            date_string = ' '.join(datetime_tweet[i].get_attribute('title').split(' · '))
            # print(type(date_string))
            # print(date_string)
            datetime_obj = datetime.datetime.strptime(date_string, '%H:%M %p %b %d, %Y')
            
            
            
            if datetime_obj > (datetime.datetime.now() - timedelta(1)):
                tweetdate.append(datetime_obj)
                tweets.append(tweet[i].text)
                
                
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    tweets_df = pd.DataFrame({'tweets': tweets})

    temptweet = []
    temptweet.append(' '.join(tweets))
        
    # temptweet.append(tweetsofday)

    from sklearn.feature_extraction.text import TfidfVectorizer
    import joblib
    from sklearn.naive_bayes import GaussianNB

    loaded_pkl = joblib.load("TDIDFvector.pkl")

    trumptweet = loaded_pkl.transform(temptweet)

    loaded_GNB = joblib.load("GNB.pkl")

    outcome = loaded_GNB.predict(trumptweet.todense())
    
    # Close the browser after scraping
    driver.quit()

    # print(outcome[0])

    driver = webdriver.Chrome()
    url = 'https://www.google.com/search?q=S%26P+500&oq=S%26P+500&aqs=chrome..69i57j69i61.6436j0j4&sourceid=chrome&ie=UTF-8'

    driver.get(url)

    time.sleep(1)

    SP = driver.find_elements_by_xpath("//g-card-section/div/g-card-section/span[2]/span")
    stock=(SP[0].text)
    # dic = {'outcome':outcome[0], 'stock':stock}
    driver.quit()

    df = pd.DataFrame({'outcome': outcome, 'stock': stock}, index=[0])
    
    return df
    # return stock

if __name__ == '__main__':
    scrape_info()
# # Dependencies
# import os
# import pandas as pd
# from splinter import Browser
# from bs4 import BeautifulSoup as bs
# import numpy as np
# import re
# import datetime
# from datetime import timedelta
# import time
# from selenium import webdriver

# def stock_info():
#     driver = webdriver.Chrome()
#     url = 'https://www.google.com/search?q=S%26P+500&oq=S%26P+500&aqs=chrome..69i57j69i61.6436j0j4&sourceid=chrome&ie=UTF-8'

#     driver.get(url)

#     time.sleep(1)

#     SP = driver.find_elements_by_xpath("//g-card-section/div/g-card-section/span[2]/span")
#     SP500=(SP[1].text)
   
    
#     driver.quit()
    
#     # print(SP500)

# if __name__ == '__main__':
#     stock_info()
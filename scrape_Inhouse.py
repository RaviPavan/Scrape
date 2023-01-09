#https://www.geeksforgeeks.org/how-to-install-selenium-on-macos/
#pip3 install bs4


from datetime import *
import time 
from threading import Thread 
import os,random,sys,time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import requests

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
"""

op = webdriver.ChromeOptions()
#op.add_argument('headless')
s = Service('/users/ravipavn/Downloads/chromedriver')
    #driver = webdriver.Chrome(service=s)
browser=webdriver.Chrome(service=s,options=op)
browser.get('https://www.google.com/search?q=https://in.linkedin.com/in/sai-sarthak-dash-9794591a8')
elementID=browser.find_element(By.CLASS_NAME,'yuRUbf')
print(elementID)
elementID.submit()
"""
# Sending HTTP request 
request_result = requests.get( 'https://www.google.com/search?q=https://in.linkedin.com/in/sai-sarthak-dash-9794591a8' )

  
# Pulling HTTP data from internet 
soup = BeautifulSoup( request_result.text 
                         , "html.parser" )
print(soup)
print("Done")

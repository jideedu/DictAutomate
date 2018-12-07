'''
this script loads an html file 'web.html' and searches all alexa utterance 
voice to text translations, and prints them.

This script should be modified to access the website automatcally and keep jumping page to page downloading and parsing the website.
So this code could be all found inside a function tat is called very time a new website is opened and parsed
'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import urllib.request
import re

driver = webdriver.Firefox(executable_path="C:\\Users\\k1772492\\Downloads\\chromedriver_win32\\geckodriver.exe")

#def get2():
        #webdriver.executeScript("var f = document.createElement('div').appendChild(arguments[0].cloneNode(true))
        #return f.parentNode.innerHTML", element);

def Url():
        #quote_page = "web.html"
        # Create a new instance of the Google driver
        
        #driver.maximize_window()
        
        # go to the Amazon Privacy URL
        driver.get("https://www.amazon.co.uk/hz/mycd/myx/#/home/alexaPrivacy/home&today")

        # filling the login in form
        driver.find_element_by_id('ap_email').send_keys('jideedu@gmail.com')
        driver.find_element_by_id('ap_password').send_keys('')
        driver.find_element_by_id('signInSubmit').click()

        #Clicking on the privacy tab
        time.sleep(3)
        python_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]/div[6]")
        python_button.click()
        time.sleep(3)
        python_button2 = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[5]/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[3]")
        python_button2.click()


        #waiy for the hidden div to load
        time.sleep(1)

        #finding one of the hidden attribute
        demo_div = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div[5]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div/div/div/div[7]/div/div[3]/div/div[1]/div[1]/span[1]/div")

        #this find the attribute link to the copy xpath
        demo_div.get_attribute('innerHTML')

        #this execute the script to the copy xpath
        driver.execute_script("return arguments[0].innerHTML", demo_div)

        #this find the textContent link to the copy xpath
        demo_div.get_attribute('textContent')

        #this execute the script to the copy xpath
        driver.execute_script("return arguments[0].textContent", demo_div)


        
        quote_page = driver.page_source
        
        #print(quote_page)
        #print('data {}'.format(quote_page))
        return quote_page

def findAllUtterances(data):

        soup = bs(data, "html.parser")
        
        voice_comms = soup.findAll("div", attrs={"class": "textInfo"})
        time.sleep(5)
        #print (voice_comms)
        c = 0
        time.sleep(10)
        for el in voice_comms:
                #time.sleep(15)
                #We are trying to find the utterance text in the website
                msg = el.find("div", attrs={"class":"summaryCss"})		
                if(msg):
                        msg = msg.text.strip()
                else:
                        msg = el.find("div", attrs={"class":"summaryNotAvailableCss"}).text.strip()
                #time.sleep(15)
		#datettime of the utterance
                datetime = el.find("span", attrs={"class":"subInfo"}).text.strip()		
                #time.sleep(10)
                print('\n\n {} - {} \n {}'.format(c, datetime, msg ))
                c+=1




data = Url()
#with open(quote_page, 'r', encoding='utf8') as myfile:
#data = myfile.read()
findAllUtterances(data)
#python_button3 = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div/div/div/div[5]/div/div/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[2]/div[3]')
#python_button3.click()

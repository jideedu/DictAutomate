#import unittest

import sys
from bs4 import BeautifulSoup as bs
import re
import time
import datetime
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Dicto(my_list):
         
    # Create a new instance of the Google driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\SHAM.SHAM-PC\\Desktop\\Chromes\\chromedriver.exe")

    #Loading the Dictionary File
    inFile = open('C:\\Users\\SHAM.SHAM-PC\\Desktop\\british-english1.txt', "r")
   
    count = 0
    numb = 0
    #my_list = list()
    #Loading the word
    for x in inFile:
        if x not in my_list:
            my_list.append(x)
            # go to the tophonetics.com homepage
            driver.get("https://tophonetics.com/")
            driver.find_element_by_name("text_to_transcribe").send_keys(x)

            # submit the form
            #inputElement.submit()
            
            count = count + 1
            numb = numb + 1                    
            try:
                #show the transcription
                
                driver.find_element_by_name("submit").click()            
                # click UK pronounciation button using the Xpath

                #pronounciation without repetation
                python_button = driver.find_element_by_xpath('//*[@id="play"]').click()
                time.sleep(2)
                
                #To repeat pronounciation twice
                #python_button = driver.find_element_by_xpath('//*[@id="play"]')
                #for i in range(2):
                    #python_button.click()
                    #time.sleep(5)                           
            except:
                print (x + " is not in the dictionary!")

            page = driver.page_source
            #rectify the UCS2 codec error
            non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
            quote_page = (page.translate(non_bmp_map))        
           
            if count==1000:
                break
            findAllUtterances(quote_page, numb)
    driver.quit()
    inFile.close()


def findAllUtterances(data, number):
        soup = bs(data, "html.parser")
        #time.sleep(5)
        word = soup.find("div", attrs={"class": "textarea_wrapper"})
        word = word.get_text().strip()
        trans = soup.find("div", attrs={"id": "transcr_output"})
        trans = trans.get_text().strip()
        a = datetime.datetime.now()
        f = open('newlog','a+')
        f.write('{} {}  {}  {}\n'.format(number,word ,trans, a))


def skillinvoke():
    # Create a new instance of the Mozilla driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\SHAM.SHAM-PC\\Desktop\\Chromes\\chromedriver.exe")
       
    # go to the naturalreaders home page
    driver.get("https://www.naturalreaders.com/online/")
    inputElement = driver.find_element_by_xpath('//*[@id="inputDiv"]').clear()

    # type in the search
    inputElement = driver.find_element_by_xpath('//*[@id="inputDiv"]')
    time.sleep(2)
    inputElement.send_keys("Alexa, repeat me")

    # click UK pronounciation button using the Xpath
    python_button2 = driver.find_element_by_xpath('//*[@id="pw_wrapper"]/div[2]/div[1]/div[2]/app-reader/div[1]')
    python_button2.click()
    time.sleep(4)        
    driver.quit()
  
my_list = list()
while True:    
    Dicto(my_list)
    skillinvoke()
    
    

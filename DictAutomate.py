#import unittest

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Repeat the whole process twice
for x in range(2):
    # Create a new instance of the Google driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\SHAM.SHAM-PC\\Desktop\\Chromes\\chromedriver.exe")
    # Create a new instance of the Firefox driver
    #driver = webdriver.Firefox(executable_path="C:\\Users\\k1772492\\Downloads\\chromedriver_win32\\geckodriver.exe")

    #Loading the Dictionary File from your system
    inFile = open('C:\\Users\\SHAM.SHAM-PC\\Desktop\\dict2.txt', "r")

    #Skip the first line to avoid error
    #first_line = inFile.readline()
    
    #Looping through the word
    for x in inFile:
       
        # go to the cambridge Dictionary home page
        driver.get("https://dictionary.cambridge.org/dictionary/english/")
        inputElement = driver.find_element_by_name("q")

        # type in the search
        inputElement.send_keys(x)

        # submit the form (necessasry for Mozilla firefox browser)
        #inputElement.submit()
        try:
           

            # the page is ajaxy so the title is originally this:
            print (driver.title)

            #try:
            # we have to wait for the page to refresh, the last thing that seems to be updated is the title
            #WebDriverWait(driver, 10).until(EC.title_contains(x))

            #needed for firefox driver
            time.sleep(3)
            #finally:
            # click UK pronounciation button using the Xpath
            python_button = driver.find_element_by_xpath('//*[@id="dataset-cald4"]/div[3]/div/div[2]/div/div/div[1]/div[1]/span[1]/span[1]/span[2]')
            #To repeat pronounciation
            for i in range(2):
                python_button.click()
                time.sleep(3)
            time.sleep(5)    
            
        except:
            print (x + " is not in the dictionary!")
            time.sleep(2)

    driver.quit()   

import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Dicto(my_list):
         
    # Create a new instance of the Google driver
    driver = webdriver.Firefox(executable_path="C:\\Users\\*******8\\Downloads\\chromedriver_win32\\geckodriver.exe")

    #Loading the Dictionary File
    inFile = open('C:\\Users\\********\\Downloads\\chromedriver_win32\\dicts\\british-english_clean', "r")  
    #Skip the first line to avoid error
    #first_line = inFile.readline()
    
    # To count the number of file pronounced
    count = 0

    #Loading the word
    for x in inFile:
        if x not in my_list:
            my_list.append(x)
            # go to the cambridge Dictionary home page
            driver.get("https://dictionary.cambridge.org/dictionary/english/")
            inputElement = driver.find_element_by_name("q")

            # type in the search
            inputElement.send_keys(x)

            # submit the form
            inputElement.submit()
            
            count = count + 1
                                
            try:
           

                # the page is ajaxy so the title is originally this:
                print (driver.title)
                
                #Open a Log file
                with open('Logee.txt', "a+") as f:
                    f.write("%s \n" %(driver.title))
            
                #try:
                # we have to wait for the page to refresh, the last thing that seems to be updated is the title
                #WebDriverWait(driver, 10).until(EC.title_contains(x))

                # You should see the world"
                #print (driver.title)

                time.sleep(3)
                #finally:
                # click UK pronounciation button using the Xpath
                python_button = driver.find_element_by_xpath('//*[@id="dataset-cald4"]/div[3]/div/div[2]/div/div/div[1]/div[1]/span[1]/span[1]/span[2]')
                #To repeat pronounciation
                for i in range(2):
                    python_button.click()
                    time.sleep(5)
                #time.sleep(5)
                           
            except:
                print (x + " is not in the dictionary!")
                #time.sleep(2)
            
            #Checking the number of words pronounced
            if count==15:
                break
        
        
    
    driver.quit()
    #f.close()
    inFile.close()


def skillinvoke():
    # Create a new instance of the Google driver
    driver = webdriver.Firefox(executable_path="C:\\Users\\********\\Downloads\\chromedriver_win32\\geckodriver.exe")
       
    # go to the naturalreaders home page
    driver.get("https://www.naturalreaders.com/online/")
    inputElement = driver.find_element_by_xpath('//*[@id="inputDiv"]').clear()

    # type in the search
    inputElement = driver.find_element_by_xpath('//*[@id="inputDiv"]')
    time.sleep(1)
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
    
    

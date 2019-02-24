""" The below code is to test the Privacy link in the qainterview page """
# importing time and webdriver
import time
from selenium import webdriver
# intializing the Firefox webdriver
driver = webdriver.Firefox()
# Opening the qainterview page in the browser
driver.get('https://qainterview.pythonanywhere.com/')
# Finding the Privacy link by xpath and calling the Click function to click the link
driver.find_element_by_xpath("//a[@href='/terms']").click()
# Setting 3 sec time before the next line of code is run
time.sleep(3)
# Validating if the current URL is https://qainterview.pythonanywhere.com/terms and printing success or Failure
if (driver.current_url== 'https://qainterview.pythonanywhere.com/terms'):
    print ("Success")
else:
    print ("Failure")   

# Close the browser   
driver.close()

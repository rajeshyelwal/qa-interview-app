""" The below code is to test the Qxf2 link link in the qainterview page """
# importing time and webdriver
import time
from selenium import webdriver
# intializing the Firefox webdriver
browser = webdriver.Firefox()
# Opening the qainterview page in the browser
browser.get('https://qainterview.pythonanywhere.com/')
# Finding the Qxf2 link by xpath and calling the Click function to click the link
browser.find_element_by_xpath("//a[@href='https://www.qxf2.com/?utm_source=qa-interview&utm_medium=click&utm_campaign=From%20QA%20Interview']").click()
time.sleep(3)
# Validating if the title of page is Qxf2 Services: Outsourced Software QA for startups
if(browser.title=="Qxf2 Services: Outsourced Software QA for startups"):
    print ("Success: Qxf2 home page launched successfully")
else:
    print ("Failed: Qxf2 home page Title is incorrect") 

# Quit the browser window
browser.quit() 


""" The below code is to test the factorial of a number """
#importing time and webdriver
import time
from selenium import webdriver
#intializing the Firefox webdriver
driver = webdriver.Firefox()
#Opening the qainterview page in the browser
driver.get('https://qainterview.pythonanywhere.com/')

#Finding the element 'number' by a id 
name = driver.find_element_by_id('number')
time.sleep(3)
#Assigning a value to the number field
name.send_keys('3')
#Setting 3 sec time before the next line of code is run
time.sleep(3)
#Clicking the Calcualte button, by finding the element by its xpath and calling the click function
button = driver.find_element_by_xpath("//button[text()='Calculate!']").click()

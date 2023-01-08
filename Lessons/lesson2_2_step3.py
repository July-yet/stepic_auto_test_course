from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 =int(browser.find_element(By.ID, "num2").text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    summ = num1+num2
    select.select_by_value(str(summ))    
    
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()    
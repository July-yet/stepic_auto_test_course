from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    input_1 = browser.find_element(By.NAME, "firstname")
    input_1.send_keys("Ivanov")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivan")
    input3= browser.find_element(By.NAME, "email")
    input3.send_keys("ivan@bk.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file_demo.txt")
    input_file = browser.find_element(By.NAME, "file")
    input_file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")    
    button.click()
    

finally:
    time.sleep(15)
    browser.quit()    